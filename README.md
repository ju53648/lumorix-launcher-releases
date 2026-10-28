<div align="center">

# VENSUKO Launcher

**Games. Software. Beyond.**

Your games, downloads and updates in one desktop launcher.

[![Latest release](https://img.shields.io/badge/latest%20release-0.13.1-15897b)](https://github.com/ju53648/lumorix-launcher-releases/releases/latest)
![Windows](https://img.shields.io/badge/Windows-x64-263444)
![macOS](https://img.shields.io/badge/macOS-Intel%20%2B%20Apple%20Silicon%20test%20builds-263444)
![Official downloads](https://img.shields.io/badge/source-official%20downloads-263444)

### [Download VENSUKO Launcher for Windows](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_x64-setup.exe)

**Current version: 0.13.1** · [Release notes](https://github.com/ju53648/lumorix-launcher-releases/releases/tag/v0.13.1)

</div>

---

## Download

### Windows · 64-bit

**[Download VENSUKO Launcher 0.13.1 (.exe)](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_x64-setup.exe)**

1. Download the Windows installer above.
2. Run the installer and launch VENSUKO.
3. Future launcher updates are checked through the built-in signed updater.

### macOS - Intel (2018/2019 MacBooks etc.) and Apple Silicon (M1 and newer)

**Early test builds, not notarized by Apple.**

| Mac | Download | SHA-256 |
| :--- | :--- | :--- |
| Intel (x64) | [VENSUKO 0.13.1 for Intel Mac (.dmg)](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_macos-x64.dmg) | [Checksum](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_macos-x64.dmg.sha256) |
| Apple Silicon (arm64) | [VENSUKO 0.13.1 for M-series Mac (.dmg)](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_macos-arm64.dmg) | [Checksum](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_macos-arm64.dmg.sha256) |

These are **ad-hoc-signed, non-notarized builds**, not an Apple-certified release. macOS Gatekeeper may require approval for the individual application in **System Settings > Privacy & Security > Open Anyway**. Never disable Gatekeeper globally. A complete physical-Mac sign-in/Keychain test is still pending; please report issues. **The macOS launcher currently updates manually.** Windows-only games such as PORTLORIA are shown as Windows-only and cannot be installed on Mac until native game builds exist.

## What's new in version 0.13.1?

- **Interface sound volume starts at 100%** for new installations. You can lower it or turn it off at any time.
- Redesigned, clearer sounds with **14 distinct short cues** for navigation, toggles, confirmation, cancellation, selection, opening/closing, errors, game launch and downloads.
- Dedicated sound feedback for updates and notifications.
- Three sound previews in the settings panel; German, English and Polish supported.
- Already saved volume preferences are preserved. The game audio is unaffected.

## Official release files

| File | Purpose |
| :--- | :--- |
| `VENSUKO.Launcher_0.13.1_x64-setup.exe` | Windows 64-bit installer |
| `VENSUKO.Launcher_0.13.1_x64-setup.exe.sig` | Signature for the built-in Tauri updater |
| `latest.json` | Automatic Windows update manifest |
| `VENSUKO.Launcher_0.13.1_macos-x64.dmg` | Intel Mac test installer (not notarized) |
| `VENSUKO.Launcher_0.13.1_macos-arm64.dmg` | Apple Silicon Mac test installer (not notarized) |
| `*.dmg.sha256` | SHA-256 checksums for both Mac installers |

> **Windows security notice:** Windows may display an *Unknown publisher* warning because the installer does not yet carry a trusted Authenticode publisher certificate. The `.exe.sig` file is for verifying launcher updates; it is not a Windows publisher certificate.

## Official links

[**All releases**](https://github.com/ju53648/lumorix-launcher-releases/releases) · [**Public game catalog**](https://github.com/ju53648/lumorix-launcher-content) · [**Lumorix website**](https://lumorix.net)

<details>
<summary><strong>Deutsch – VENSUKO herunterladen</strong></summary>

**VENSUKO Launcher 0.13.1 für Windows (64 Bit):** [Installer direkt herunterladen](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_x64-setup.exe).

Die Oberflächensounds sind jetzt deutlich hörbarer. Für neue Installationen ist die **Lautstärke standardmäßig auf 100 %** eingestellt; bereits gespeicherte Einstellungen bleiben erhalten. 14 verschiedene kurze Klänge decken Navigation, Schalter, Bestätigung, Abbrechen, Downloads und Meldungen ab. Drei Hörproben stehen in den Einstellungen bereit.

**Mac-Testversion:** [Intel-Mac herunterladen](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_macos-x64.dmg) oder [Apple Silicon herunterladen](https://github.com/ju53648/lumorix-launcher-releases/releases/download/v0.13.1/VENSUKO.Launcher_0.13.1_macos-arm64.dmg). Diese macOS-Version ist noch **nicht von Apple notarisiert**. macOS kann daher beim ersten Start eine Freigabe der einzelnen App unter **Systemeinstellungen > Datenschutz & Sicherheit** verlangen. Anmeldung und SchlÃ¼sselbund werden noch auf echten Macs getestet; Mac-Updates erfolgen vorerst manuell.
Bei der Installation kann Windows eine Warnung wegen eines unbekannten Herausgebers anzeigen. Die separate Updater-Signatur ist keine Windows-Herausgebersignatur.

</details>

---

<sub>This is the official **distribution-only repository**. Application source, credentials and internal development files remain private.</sub>
