<div align="center">

# VENSUKO Launcher

**Games. Software. Beyond.**

Your games, downloads and updates in one desktop launcher.

[![Windows version](https://img.shields.io/badge/Windows-0.14.2-263444)](https://github.com/ju53648/lumorix-launcher-releases/releases/tag/v0.14.2)
[![macOS version](https://img.shields.io/badge/macOS-0.14.2%20Beta-15897b)](https://github.com/ju53648/lumorix-launcher-content/releases/tag/vensuko-launcher-v0.14.2-macos)
![Mac CPUs](https://img.shields.io/badge/macOS-Intel%20%2B%20Apple%20Silicon-263444)
![Official downloads](https://img.shields.io/badge/source-official%20downloads-263444)

### [Download for Windows](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.14.2/VENSUKO.Launcher_0.14.2_x64-setup.exe) · [Download for Mac](https://github.com/ju53648/lumorix-launcher-content/releases/tag/vensuko-launcher-v0.14.2-macos)

**Synchronized version, separate native packages:** Windows 0.14.2 · macOS 0.14.2 Beta. Mac builds are publicly released in [VENSUKO's public content repository](https://github.com/ju53648/lumorix-launcher-content/releases).

</div>

---

## Downloads

### Windows 64-bit — v0.14.2

**[Download Windows installer (.exe)](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.14.2/VENSUKO.Launcher_0.14.2_x64-setup.exe)**

Windows launcher updates use their separate signed updater feed.

### macOS — v0.14.2 Beta

| Mac processor | Installer | SHA-256 checksum |
| :--- | :--- | :--- |
| **Apple Silicon** (M1, M2, M3, M4, M5) | **[Download Apple Silicon (.dmg)](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.14.2-macos/VENSUKO.Launcher_0.14.2_macos-arm64.dmg)** | [Verify checksum](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.14.2-macos/VENSUKO.Launcher_0.14.2_macos-arm64.dmg.sha256) |
| **Intel** (x64) | **[Download Intel Mac (.dmg)](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.14.2-macos/VENSUKO.Launcher_0.14.2_macos-x64.dmg)** | [Verify checksum](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.14.2-macos/VENSUKO.Launcher_0.14.2_macos-x64.dmg.sha256) |

To identify the processor, choose **Apple menu → About This Mac**.

**Already using Mac version 0.13.3?** Open **About → Check for updates** to install 0.14.2 from the signed macOS feed. If the updater has not refreshed yet, download the 0.14.2 DMG above and replace the existing application in Applications. Older 0.13.1/0.13.2 builds cannot update automatically; use the DMG. Games and cloud profiles remain unchanged. Mac users should sign in again once after the 0.14.2 migration. Previously stored Keychain entries are not touched, and new sessions use one OS-secured credential instead of multiple individual entries. Ad-hoc signing may still trigger a permission prompt after future Mac updates; permanent Apple Developer signing is planned.

**macOS security:** These are ad-hoc-signed, non-notarized beta builds, not Apple Developer ID-certified releases. The first launch may require approval for the individual app in **System Settings → Privacy & Security → Open Anyway**. Do not disable Gatekeeper globally. Full physical-Mac Keychain/login and auto-update testing is still ongoing.

Some games require their own native macOS builds. For example, PORTLORIA's Windows-only build does not become Mac-compatible merely by installing the Mac launcher.

## Release channels

- [**Windows stable releases**](https://github.com/ju53648/lumorix-launcher-releases/releases)
- [**macOS public releases (Intel and Apple Silicon)**](https://github.com/ju53648/lumorix-launcher-content/releases)
- [**macOS automatic updater feed**](https://raw.githubusercontent.com/ju53648/lumorix-launcher-content/main/distribution/updates/macos/latest.json)
- [**Public game catalog**](https://github.com/ju53648/lumorix-launcher-content)

## What's new?

**Windows and macOS 0.14.2:** Fixed account sign-out errors caused by rejected authentication storage keys. The Mac version stores each authenticated session in one isolated Keychain entry rather than dozens of shards and caches repeated lookups in memory. macOS users sign in once after upgrading; existing Keychain entries stay untouched. Game cloud synchronization remains disabled until version 1.0.0 and the dedicated server are ready.

**Unified version policy:** Both OSes must pass independent builds and signature verification before the next public version is announced. They use separate native installers and update feeds, not separate app version numbers.

## Installation and security notes

- **Windows:** Windows SmartScreen may show an *Unknown publisher* warning because the installer is not Authenticode-signed by a trusted publisher. A Tauri update signature is not an Authenticode publisher certificate.
- **Mac:** Quit an older VENSUKO version, open the latest DMG, and copy VENSUKO Launcher into Applications, replacing the existing copy when prompted. Check **About VENSUKO** to confirm v0.14.2.
- **Updates:** The launcher can only install versions that are actually built, signed, and made available on its platform's official update feed.

<details>
<summary><strong>Deutsch – VENSUKO herunterladen</strong></summary>

**Windows 64 Bit (0.14.2):** [Installer herunterladen](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.14.2/VENSUKO.Launcher_0.14.2_x64-setup.exe).

**macOS (0.14.2 Beta):** [Apple Silicon (M1–M5)](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.14.2-macos/VENSUKO.Launcher_0.14.2_macos-arm64.dmg) · [Intel-Mac](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.14.2-macos/VENSUKO.Launcher_0.14.2_macos-x64.dmg).

**Wichtig:** Wer noch 0.13.1 oder 0.13.2 auf dem Mac verwendet, muss 0.13.3 einmal manuell installieren. Erst danach kann der Launcher zukünftige veröffentlichte und signierte Mac-Updates automatisch installieren.

Die Mac-Testversion ist noch **nicht von Apple notarisiert**. Falls nötig, lässt sich die einzelne App unter **Systemeinstellungen → Datenschutz & Sicherheit** freigeben. Bitte nicht Gatekeeper insgesamt deaktivieren.

**Alle neuen Mac-Releases:** [VENSUKO macOS-Veröffentlichungen](https://github.com/ju53648/lumorix-launcher-content/releases).

</details>

---

<sub>Official **distribution-only repository**. The application source, signing credentials, and internal development files remain private.</sub>
