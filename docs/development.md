# Development

Install uv, then run the three commands at the start of the
[README](../README.md). `.python-version` selects Python 3.13 for development;
the application supports Python 3.13 and newer. CI checks 3.13 and 3.14.

`uv run inv setup` uses `uv sync --locked`. Add runtime dependencies with
`uv add PACKAGE` and development tools with `uv add --dev PACKAGE`; retain both
pyproject.toml and uv.lock. Review upgrades deliberately, verify current Flet MCP
contracts, then run `uv run inv check` and a real build. Flet runtime, CLI extras,
and MCP are pinned together to stable 1.0.1 in this template.

Use `uv run inv run` for desktop or `uv run inv run-web` for browser development.
Both hot-reload the source tree. Stop with Ctrl+C. Web binds to localhost, not the
LAN. Debug variants and log locations are documented in [debugging](debugging.md).
`.env.example` is documentation, not automatically loaded configuration. Set
variables in your shell/IDE; keep local `.env` files out of version control.

## Packaging

All builds go through Invoke so asset staging, icon validation, host checks, and
release debug-marker removal happen consistently. `build-local` maps Linux to
Linux, Windows to Windows, and Darwin to macOS; it does not emulate another OS.
Platform-specific tasks reject incompatible hosts before starting a build.

| Tasks | Host / tools | Output |
| --- | --- | --- |
| `build-web` | Linux, Windows, macOS; Flutter | `build/web` |
| `build-android`, `build-android-aab` | Linux, Windows, macOS; JDK 17, Android SDK | `build/apk`, `build/aab` |
| `build-ios` | macOS; Xcode 15+, CocoaPods 1.16+, provisioning/certificates | `build/ipa` |
| `build-ios-simulator` | macOS; Xcode and CocoaPods, no signing required | `build/ios-simulator` |
| `build-macos` | macOS; Xcode and CocoaPods | `build/macos` |
| `build-windows` | Windows; Visual Studio Desktop development with C++ | `build/windows` |
| `build-linux` | Linux; Clang, CMake, Ninja, pkg-config, GTK development packages | `build/linux` |

Flet installs its required Flutter version when unavailable. It can install JDK
and Android SDK components too; allow disk space, downloads, and SDK licensing.
For Debian/Ubuntu Linux builds, the CI packages are `clang cmake ninja-build
pkg-config libgtk-3-dev liblzma-dev libstdc++-12-dev`. Plugins may add native
requirements. A WSL Linux environment builds Linux, not Windows; GUI use needs
WSLg or an appropriate display. On Apple Silicon some tools require Rosetta.
Run `uv run inv doctor` to inspect the actual host.

Flet selects the highest bundled Python satisfying `requires-python` (currently
3.14.7 for this range), not necessarily the local 3.13 interpreter. Web uses the
corresponding Pyodide runtime. Check Flet's build output when upgrading; add an
explicit supported build Python version only if a dependency requires it. Native
extensions need target-specific Android/iOS wheels or Pyodide support. Desktop
installation success alone is not proof of mobile/browser compatibility.

uv.lock fixes the development environment. Flet's target packager separately
resolves `[project].dependencies`; it does not consume uv.lock as a target lock.
Runtime Flet is pinned, but transitive target dependencies may still change.
Retain build logs/artifacts and test packaged outputs before releases. Do not
describe builds as bit-for-bit reproducible based on uv.lock alone.

Release app sources are precompiled (`compile.app=true`). Flet's packager removes
original `.py` files during compilation even when `cleanup.app=false`; traceback
frames still retain function/file/line information, but source text is absent.
Mobile debug disables app compilation for source-rich diagnostics. Local Flet
storage is excluded from packaging and hot reload. Generated output is ignored.
`uv run inv clean` removes builds and staging/caches, not the canonical icon,
virtual environment, or local Flet user data.

## Signing and CI

Android builds without a configured upload key use a debug key and cannot go to
Google Play. `build-ios` may produce only an unsigned archive without configured
certificates/profiles; an installable/exportable IPA needs matching signing.
macOS local builds are ad-hoc signed; public distribution normally needs Developer
ID signing and notarization. Configure platform metadata in pyproject.toml, but
keep passwords, key files, and credentials in external stores or CI secrets.

Push/PR CI runs format-check, lint, Pyright, and pytest on Python 3.13/3.14. Manual
workflow dispatch adds web, APK/AAB, Linux, Windows, macOS, and unsigned iOS
simulator builds on the proper runners. It does not publish or install signing
secrets. A green simulator job does not certify a physical device or store release.

References: [Flet publishing](https://flet.dev/docs/publish/),
[Android](https://flet.dev/docs/publish/android),
[iOS](https://flet.dev/docs/publish/ios),
[Linux](https://flet.dev/docs/publish/linux),
[Windows](https://flet.dev/docs/publish/windows),
[macOS](https://flet.dev/docs/publish/macos).