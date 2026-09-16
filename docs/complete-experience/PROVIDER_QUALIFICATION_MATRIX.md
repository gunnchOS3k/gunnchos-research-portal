# Software Provider Qualification Matrix (summary)

Full data: `PROVIDER_QUALIFICATION_MATRIX.json`.

**Policy:** zero-additional-license-cost candidates only; **do not standardize** until compatibility demonstrated.

| Provider | CX0 status | Key blockers |
|----------|------------|--------------|
| LibreOffice | DIGITAL_CANDIDATE | MS Office fidelity EXTERNAL |
| Chromium/Firefox | DIGITAL_CANDIDATE | PWA lifecycle manager ABSENT |
| Thunderbird | CANDIDATE | Not selected (PWA fallback today) |
| Blender | UNQUALIFIED | Not packaged; GPU/ARM |
| Godot | PARTIAL_VIA_GAMES | Editor not productized |
| KiCad | DIGITAL_SOT_EXTERNAL | Hardware SoT; Device OS lane missing |
| Krita/Inkscape/GIMP | UNQUALIFIED | Missing in G15 guest |
| Kdenlive/OBS/Audacity/Ardour | UNQUALIFIED | Not packaged; portal/JACK |
| FreeCAD | UNQUALIFIED | Not packaged |
| Podman | CANDIDATE | Workstation image missing |
| VSCodium/neovim | DIGITAL_CANDIDATE | Builder mode incomplete |


## CX1 ordinary-user digital foundations

| Provider | Status | Notes |
|----------|--------|-------|
| Local FS Vault | DIGITAL_PASS | Product file authority |
| Local backup + integrity | DIGITAL_PASS | Journey 5 |
| Durable sync queue | DIGITAL_PASS | Survives restart |
| Flatpak | DIGITAL_PARTIAL | Fail closed when absent |
| xdg-desktop-portal | DIGITAL_PARTIAL | Fail closed when absent |
| LibreOffice | DIGITAL_PARTIAL | Host-dependent |
| System browser | DIGITAL_PARTIAL | Not standardized as default |
| CUPS virtual PDF | DIGITAL_PASS | Physical print PHYSICAL_PENDING |
| Thunderbird | DIGITAL_PARTIAL | Fail closed when absent |
| Gmail/Outlook | EXTERNAL_PROVIDER_PENDING | Not claimed |

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`
