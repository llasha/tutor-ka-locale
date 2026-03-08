# tutor-ka-locale

This is a basic v1 plugin for **Tutor v21** that enables adding a new (previously unsupported) language locale (e.g., Georgian `ka`) to the **Django (backend) side** of Open edX.

This plugin affects only the LMS/CMS Django translation layer.  
MFE translations must be handled separately (see the companion plugin:  
https://github.com/llasha/tutor-ka-localization).

---

## Purpose

Open edX pulls official translations from Transifex via Atlas.  
If a locale does not yet exist upstream, this plugin allows you to:

- Register a new Django locale
- Inject compiled translation files
- Rebuild Open edX with backend language support

---

### 0. Prepare Your Fork (Required)

Fork this repository and update the source code to include your language locale (e.g., `ka`).  
Then clone **your fork** (not the upstream repository) in the next step.

---

## Installation

### 1. Clone the Plugin

Change to the Tutor plugins directory (create it if necessary) and clone the repository:

```bash
mkdir -p "$(tutor plugins printroot)"
cd "$(tutor plugins printroot)"
git clone https://github.com/<your-user>/tutor-ka-locale
```

---

### 2. Install and Enable

```bash
cd "$(tutor plugins printroot)"
pip install -e tutor-ka-locale
tutor plugins enable ka_locale
tutor config save
```

---

## (Optional) Use a Custom `openedx-translations` Fork

Starting from Tutor v19, translations are managed by **Atlas**, which pulls files from the `openedx-translations` repository.

If you are using a fork of `openedx-translations`, set:

```bash
tutor config save \
  --set ATLAS_REPOSITORY="l1ph0x/openedx-translations" \
  --set ATLAS_REVISION="ulmo-ka.1"
```

Adjust the revision/tag as needed.

---

## Rebuild Open edX Image

Rebuild the Open edX image to apply changes:

```bash
tutor images build openedx --no-cache
```

This may take about 40 minutes.

---

## Tag and Use the New Image

After the build completes tag your image. For instance

```bash
docker tag overhangio/openedx:21.0.0 overhangio/openedx:21.0.0-ka-1
tutor config save --set DOCKER_IMAGE_OPENEDX=overhangio/openedx:21.0.0-ka-1
```

(Optional) Verify:

```bash
tutor config printvalue DOCKER_IMAGE_OPENEDX
```

---

## (Note: This should not be needed anymore, just a leftove from Teak)
# Compile Django JS Translation Catalogs

```bash
# Compile Django JS translation catalogs for locale `ka`
tutor local exec lms sh -lc "cd /openedx/edx-platform && ./manage.py lms compilejsi18n --locale=ka -v 2"

# If this command fails, the issue is in JS i18n compilation
# (validate djangojs.po before using it).

# Recollect static assets so compiled JS translations are included
tutor local exec lms sh -lc "cd /openedx/edx-platform && ./manage.py lms collectstatic --noinput"

# Verify that new JS translation files were generated and collected
tutor local exec lms sh -lc 'find /openedx -path "*/js/i18n/ka/*" -type f 2>/dev/null | head'
```

---

## Restart Tutor

```bash
tutor local stop
tutor local start -d
```

---

## Compatibility: Tested & Works With

- Tutor v21 (Ulmo)

---

## License

Licensed under the Apache License, Version 2.0 (Apache-2.0).

See the LICENSE file for details.
