<div align="center">

# VENSUKO Launcher

**Games. Software. Beyond.**

Your games, downloads and updates in one desktop launcher.

[![Windows version](https://img.shields.io/badge/Windows-0.13.1-263444)](https://github.com/ju53648/lumorix-launcher-releases/releases/tag/v0.13.1)
[![macOS version](https://img.shields.io/badge/macOS-0.13.3%20Beta-15897b)](https://github.com/ju53648/lumorix-launcher-content/releases/tag/vensuko-launcher-v0.13.3-macos)
![Mac CPUs](https://img.shields.io/badge/macOS-Intel%20%2B%20Apple%20Silicon-263444)
![Official downloads](https://img.shields.io/badge/source-official%20downloads-263444)

### [Download for Windows](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_x64-setup.exe) · [Download for Mac](https://github.com/ju53648/lumorix-launcher-content/releases/tag/vensuko-launcher-v0.13.3-macos)

**Separate release channels:** Windows stable 0.13.1 · macOS beta 0.13.3. Mac builds are publicly released in [VENSUKO's public content repository](https://github.com/ju53648/lumorix-launcher-content/releases).

</div>

---

## Downloads

### Windows 64-bit — v0.13.1

**[Download Windows installer (.exe)](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_x64-setup.exe)**

Windows launcher updates use their separate signed updater feed.

### macOS — v0.13.3 Beta

| Mac processor | Installer | SHA-256 checksum |
| :--- | :--- | :--- |
| **Apple Silicon** (M1, M2, M3, M4, M5) | **[Download Apple Silicon (.dmg)](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.13.3-macos/VENSUKO.Launcher_0.13.3_macos-arm64.dmg)** | [Verify checksum](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.13.3-macos/VENSUKO.Launcher_0.13.3_macos-arm64.dmg.sha256) |
| **Intel** (x64) | **[Download Intel Mac (.dmg)](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.13.3-macos/VENSUKO.Launcher_0.13.3_macos-x64.dmg)** | [Verify checksum](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.13.3-macos/VENSUKO.Launcher_0.13.3_macos-x64.dmg.sha256) |

To identify the processor, choose **Apple menu → About This Mac**.

**Already using Mac version 0.13.1 or 0.13.2?** Install 0.13.3 from the DMG **once** to enable macOS automatic launcher updates. The old Mac test versions cannot detect this update. VENSUKO 0.13.3 uses a separate signed macOS updater feed and can install **future correctly published and signature-verified** updates. It will not change the Windows update channel.

**macOS security:** These are ad-hoc-signed, non-notarized beta builds, not Apple Developer ID-certified releases. The first launch may require approval for the individual app in **System Settings → Privacy & Security → Open Anyway**. Do not disable Gatekeeper globally. Full physical-Mac Keychain/login and auto-update testing is still ongoing.

Some games require their own native macOS builds. For example, PORTLORIA's Windows-only build does not become Mac-compatible merely by installing the Mac launcher.

## Release channels

- [**Windows stable releases**](https://github.com/ju53648/lumorix-launcher-releases/releases)
- [**macOS public releases (Intel and Apple Silicon)**](https://github.com/ju53648/lumorix-launcher-content/releases)
- [**macOS automatic updater feed**](https://raw.githubusercontent.com/ju53648/lumorix-launcher-content/main/distribution/updates/macos/latest.json)
- [**Public game catalog**](https://github.com/ju53648/lumorix-launcher-content)

## What's new?

**macOS 0.13.3:** Signed updater archives for both Mac architectures, a dedicated public macOS update feed, native macOS game-platform handling, and automatic checks for subsequent signed updates.

**Windows 0.13.1:** Expanded UI sounds, 14 short sound cues, dedicated update/download feedback, three sound previews, and default new-installation UI sound volume at 100%. Existing saved preferences remain intact.

## Installation and security notes

- **Windows:** Windows SmartScreen may show an *Unknown publisher* warning because the installer is not Authenticode-signed by a trusted publisher. A Tauri update signature is not an Authenticode publisher certificate.
- **Mac:** Quit an older VENSUKO version, open the 0.13.3 DMG, and copy VENSUKO Launcher into Applications, replacing the existing copy when prompted. Check **About VENSUKO** to confirm v0.13.3.
- **Updates:** The launcher can only install versions that are actually built, signed, and made available on its platform's official update feed.

<details>
<summary><strong>Deutsch – VENSUKO herunterladen</strong></summary>

**Windows 64 Bit (0.13.1):** [Installer herunterladen](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_x64-setup.exe).

**macOS (0.13.3 Beta):** [Apple Silicon (M1–M5)](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.13.3-macos/VENSUKO.Launcher_0.13.3_macos-arm64.dmg) · [Intel-Mac](https://github.com/ju53648/lumorix-launcher-content/releases/download/vensuko-launcher-v0.13.3-macos/VENSUKO.Launcher_0.13.3_macos-x64.dmg).

**Wichtig:** Wer noch 0.13.1 oder 0.13.2 auf dem Mac verwendet, muss 0.13.3 einmal manuell installieren. Erst danach kann der Launcher zukünftige veröffentlichte und signierte Mac-Updates automatisch installieren.

Die Mac-Testversion ist noch **nicht von Apple notarisiert**. Falls nötig, lässt sich die einzelne App unter **Systemeinstellungen → Datenschutz & Sicherheit** freigeben. Bitte nicht Gatekeeper insgesamt deaktivieren.

**Alle neuen Mac-Releases:** [VENSUKO macOS-Veröffentlichungen](https://github.com/ju53648/lumorix-launcher-content/releases).

</details>

---

<sub>Official **distribution-only repository**. The application source, signing credentials, and internal development files remain private.</sub>
