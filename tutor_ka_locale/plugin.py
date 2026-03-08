from tutor import hooks

# ------------------------------------------------------------------
# Open edX (Django) language + locale wiring (Ulmo / Tutor v21 safe)
# ------------------------------------------------------------------

hooks.Filters.CONFIG_OVERRIDES.add_items([
    ("OPENEDX_LANGUAGES", ["en", "ka"]),
])

COMMON = r"""
TIME_ZONE = "Asia/Tbilisi"
LANGUAGE_CODE = "en"

from django.conf.locale import LANG_INFO

# Register Georgian language metadata
LANG_INFO["ka"] = dict(
    LANG_INFO.get("en", {}),
    code="ka",
    name="Georgian",
    name_local="ქართული",
    bidi=False,
)

# Ensure ("ka", "ქართული") appears in LANGUAGES
try:
    LANGUAGES
except NameError:
    LANGUAGES = ()

if ("ka", "ქართული") not in LANGUAGES:
    LANGUAGES = tuple(list(LANGUAGES) + [("ka", "ქართული")])

# Certificates (best-effort; some installs may not define this)
try:
    CERTIFICATE_TEMPLATE_LANGUAGES = dict(CERTIFICATE_TEMPLATE_LANGUAGES, ka="ქართული")
except Exception:
    pass
"""

hooks.Filters.ENV_PATCHES.add_items([
    # Runtime settings
    ("openedx-lms-common-settings", COMMON),
    ("openedx-cms-common-settings", COMMON),

    # Build-time i18n settings (optional but recommended for consistency)
    ("openedx-common-i18n-settings", COMMON),
])
