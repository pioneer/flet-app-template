# Branding

**Template branding is not release branding.** The crossed-square icon is a
neutral placeholder, not the Flet logo or a third-party mark. No finished product
identity is implied.

## Canonical Source

Maintain only [assets/icon.png](../assets/icon.png): a 1024 x 1024 PNG. Use alpha
where appropriate, with artwork filling the source canvas. Do not pre-shrink the
artwork, add platform safe-area padding, round corners for a specific OS, or bake
in an iOS/macOS frame. Flet performs target-specific scaling, masking, safe
framing, and opaque compositing.

`uv run inv icon-check` checks format and dimensions, not artistic quality.
`icon-placeholder` can regenerate the neutral icon only when absent and refuses
to overwrite existing branding. Pillow is development-only; application runtime
does not import it. The placeholder can be recognized by its gray border and X.

`[tool.flet].icon_background` in pyproject.toml provides the universal compositing
background. Change it with the icon. Use a platform override only for a genuine
platform-specific requirement; Android adaptive background has its own override.
Do not create maintained `.ico`, `.icns`, favicon, or per-density PNG sets by
default. Do not add a separate splash source unless the product needs one.
Flet may generate splash output using the icon, which is not a second maintained
source.

## Initialize an App

Update these together:

| Location | Replace |
| --- | --- |
| pyproject.toml `[project]` | name, description, version |
| pyproject.toml `[tool.flet]` | product, company, org, bundle_id, build_number, icon_background |
| src/app/config.py | `APP_NAME` |
| assets/icon.png | Project-specific artwork |
| README.md and docs | Product identity and relevant setup/status |

The package name, visible product name, organization, and bundle/application ID
serve different purposes. Choose a stable reverse-domain bundle ID you control;
changing it after release may create a different installed app/store identity.
Keep Android/iOS store records aligned. The generic Python package `app` does not
need to be renamed merely for branding.

Use an available image-generation tool when appropriate. Without one, create a
simple original project-specific temporary icon and clearly document that final
branding is outstanding. Do not leave the neutral template X and claim the new
app is branded. See [initialize-app](../skills/initialize-app/SKILL.md).

## Validate Output

Run `uv run inv icon-check`, `uv run inv check`, and an available target build.
For web inspect `build/web/favicon.png`, `build/web/icons/`, the manifest, and
the rendered app. For native platforms inspect generated launcher/window/store
assets and the installed app. Confirm they derive from your canonical image, not
the stock Flet logo, and that opacity, safe areas, contrast, and display name look
correct. Clear browser/PWA caches or reinstall when old icons persist.

Before release, search maintained source/metadata/docs for `Flet App Template`,
`flet-app-template`, `com.example`, and `Template Organization`; review intentional
historical examples separately. Verify visually that the placeholder is gone.
Generated files are never the source of truth.