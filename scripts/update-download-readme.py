#!/usr/bin/env python3
"""Refresh download links only from complete, publicly uploaded VENSUKO releases."""
import argparse
import json
import os
from pathlib import Path
import re
import sys
import urllib.request

OWNER = "ju53648"
WIN = "lumorix-launcher-releases"
MAC = "lumorix-launcher-content"
START = "<!-- VENSUKO_RELEASES_START -->"
END = "<!-- VENSUKO_RELEASES_END -->"
README = Path(__file__).resolve().parents[1] / "README.md"


def list_releases(repo):
    url = f"https://api.github.com/repos/{OWNER}/{repo}/releases?per_page=100"
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "VENSUKO-public-downloads",
               "X-GitHub-Api-Version": "2022-11-28"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=25) as response:
        result = json.load(response)
    if not isinstance(result, list):
        raise ValueError(f"Unexpected API response: {repo}")
    return result


def latest_complete(releases, repo):
    tag_re = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$" if repo == WIN
                        else r"^vensuko-launcher-v(\d+)\.(\d+)\.(\d+)-macos$")
    candidates = []
    for release in releases:
        if release.get("draft"):
            continue
        tag = release.get("tag_name", "")
        match = tag_re.fullmatch(tag)
        if not match:
            continue
        version = ".".join(match.groups())
        public_url = f"https://github.com/{OWNER}/{repo}/releases/tag/{tag}"
        if release.get("html_url") != public_url:
            continue
        prefix = f"https://github.com/{OWNER}/{repo}/releases/download/"
        assets = {
            a["name"]: a["browser_download_url"]
            for a in release.get("assets", [])
            if a.get("state") == "uploaded" and a.get("size", 0) > 0
            and isinstance(a.get("name"), str)
            and isinstance(a.get("browser_download_url"), str)
            and a["browser_download_url"].startswith(prefix)
        }
        if repo == WIN:
            names = ["latest.json", f"VENSUKO.Launcher_{version}_x64-setup.exe",
                     f"VENSUKO.Launcher_{version}_x64-setup.exe.sig"]
        else:
            names = [f"VENSUKO.Launcher_{version}_macos-{cpu}.{ext}"
                     for cpu in ("arm64", "x64")
                     for ext in ("dmg", "dmg.sha256", "app.tar.gz", "app.tar.gz.sig")]
        if all(n in assets for n in names):
            candidates.append((tuple(map(int, match.groups())), version, public_url, assets))
    if not candidates:
        raise RuntimeError(f"No complete verified public release for {repo}")
    _, version, url, assets = max(candidates, key=lambda x: x[0])
    return version, url, assets


def render(windows, mac):
    wv, wr, wa = windows
    mv, mr, ma = mac
    wf = f"VENSUKO.Launcher_{wv}_x64-setup.exe"
    af = f"VENSUKO.Launcher_{mv}_macos-arm64.dmg"
    xf = f"VENSUKO.Launcher_{mv}_macos-x64.dmg"
    wu, au, xu = wa[wf], ma[af], ma[xf]
    lines = [
        "<!-- Auto-generated from actual public GitHub Releases. Do not edit manually. -->",
        "",
        f"[![Windows version](https://img.shields.io/badge/Windows-{wv}-263444)]({wr})",
        f"[![macOS version](https://img.shields.io/badge/macOS-{mv}%20Beta-15897b)]({mr})",
        "![Mac CPUs](https://img.shields.io/badge/macOS-Intel%20%2B%20Apple%20Silicon-263444)",
        "![Official downloads](https://img.shields.io/badge/source-official%20downloads-263444)",
        "",
        f"### [Download for Windows]({wu}) · [Download for Mac]({mr})",
        "",
        f"**Available:** Windows {wv} · macOS {mv} Beta. Each platform shows the newest",
        "complete public release; their version numbers may temporarily differ.",
        "",
        "## Downloads",
        "",
        f"### Windows 64-bit — v{wv}",
        "",
        f"**[Download Windows installer (.exe)]({wu})**",
        "",
        f"[Windows release notes]({wr}) · "
        "[Windows signed updater feed](https://github.com/ju53648/lumorix-launcher-releases/releases/latest/download/latest.json)",
        "",
        f"### macOS — v{mv} Beta",
        "",
        "| Mac processor | Installer | SHA-256 checksum |",
        "| :--- | :--- | :--- |",
        f"| **Apple Silicon** (M1 or newer) | **[Download Apple Silicon (.dmg)]({au})** | [Verify checksum]({ma[af + '.sha256']}) |",
        f"| **Intel** (x64) | **[Download Intel Mac (.dmg)]({xu})** | [Verify checksum]({ma[xf + '.sha256']}) |",
        "",
        "Check your processor using **Apple menu → About This Mac**.",
        "",
        f"[macOS release notes]({mr}) · "
        "[macOS signed updater feed](https://raw.githubusercontent.com/ju53648/lumorix-launcher-content/main/distribution/updates/macos/latest.json)",
        "",
        "## Release channels",
        "",
        f"- [**Latest Windows release (v{wv})**]({wr})",
        f"- [**Latest macOS release (v{mv})**]({mr})",
        f"- [All Windows releases](https://github.com/{OWNER}/{WIN}/releases)",
        f"- [All macOS releases](https://github.com/{OWNER}/{MAC}/releases)",
        f"- [Public game catalog](https://github.com/{OWNER}/{MAC})",
        "",
        "## What's new?",
        "",
        "The release notes always refer to the downloads shown here:",
        f"**[Windows {wv}]({wr})** · **[macOS {mv}]({mr})**.",
        "",
        "<details>",
        "<summary><strong>Deutsch – VENSUKO herunterladen</strong></summary>",
        "",
        f"**Windows 64 Bit (v{wv}):** [Installer herunterladen]({wu}).",
        "",
        f"**macOS (v{mv} Beta):** [Apple Silicon]({au}) · [Intel-Mac]({xu}).",
        "",
        "Windows und macOS werden separat veröffentlicht. Die Seite zeigt für jedes",
        "System automatisch die neueste vollständig veröffentlichte Version.",
        "Die Mac-Version ist noch nicht von Apple notarisiert.",
        "",
        "</details>",
    ]
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        w = latest_complete(list_releases(WIN), WIN)
        m = latest_complete(list_releases(MAC), MAC)
        print(f"Public assets verified: Windows {w[0]}; macOS {m[0]}")
        old = README.read_text(encoding="utf-8")
        if old.count(START) != 1 or old.count(END) != 1:
            raise ValueError("README requires exactly one pair of release markers")
        head, rest = old.split(START, 1)
        _, tail = rest.split(END, 1)
        new = head + START + "\n" + render(w, m) + END + tail
        if args.check:
            if old != new:
                raise RuntimeError("README download versions are out of date")
        elif old != new:
            README.write_text(new, encoding="utf-8", newline="\n")
            print("README updated")
        else:
            print("README already current")
        return 0
    except Exception as exc:
        print(f"Aborted without changing published content: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
