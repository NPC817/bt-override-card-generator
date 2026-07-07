from __future__ import annotations
import os
import yaml
from .profile import ConversionProfile
from ..utils.paths import user_data_path

_PROFILES_DIR = str(user_data_path("data", "profiles"))
_DEFAULT_MARKER = os.path.join(_PROFILES_DIR, ".default_profile")


class ProfileManager:
    _profiles: dict[str, ConversionProfile] = {}
    _active_name: str = "Default"
    _default_name: str = "Default"

    @classmethod
    def load(cls) -> None:
        cls._profiles = {"Default": ConversionProfile.default()}
        os.makedirs(_PROFILES_DIR, exist_ok=True)

        # Load persisted default marker
        cls._default_name = "Default"
        try:
            if os.path.exists(_DEFAULT_MARKER):
                with open(_DEFAULT_MARKER, encoding="utf-8") as f:
                    name = f.read().strip()
                    if name:
                        cls._default_name = name
        except OSError:
            pass

        for fname in os.listdir(_PROFILES_DIR):
            if not fname.endswith(".yaml"):
                continue
            path = os.path.join(_PROFILES_DIR, fname)
            try:
                with open(path, encoding="utf-8") as f:
                    data = yaml.safe_load(f)
                if isinstance(data, dict):
                    profile = ConversionProfile.from_dict(data)
                    cls._profiles[profile.name] = profile
            except Exception as e:
                print(f"Warning: could not load profile '{fname}': {e}")

        # Auto-activate the default profile on load
        if cls._default_name != "Default" and cls._default_name in cls._profiles:
            cls._active_name = cls._default_name

    @classmethod
    def active(cls) -> ConversionProfile:
        return cls._profiles.get(cls._active_name, ConversionProfile.default())

    @classmethod
    def set_active(cls, name: str) -> None:
        if name in cls._profiles:
            cls._active_name = name

    @classmethod
    def default_name(cls) -> str:
        """Return the name of the default profile (falls back to 'Default')."""
        if cls._default_name in cls._profiles:
            return cls._default_name
        return "Default"

    @classmethod
    def set_default(cls, name: str) -> None:
        """Persist a profile as the startup default."""
        if name not in cls._profiles and name != "Default":
            return
        cls._default_name = name
        try:
            with open(_DEFAULT_MARKER, "w", encoding="utf-8") as f:
                f.write(name)
        except OSError as e:
            print(f"Warning: could not save default profile marker: {e}")

    @classmethod
    def all_names(cls) -> list[str]:
        names = list(cls._profiles.keys())
        # Ensure Default is always first
        if "Default" in names:
            names.remove("Default")
            names.insert(0, "Default")
        return names

    @classmethod
    def get(cls, name: str) -> ConversionProfile | None:
        return cls._profiles.get(name)

    @classmethod
    def save(cls, profile: ConversionProfile) -> None:
        if profile.is_default():
            return
        cls._profiles[profile.name] = profile
        path = os.path.join(_PROFILES_DIR, f"{_safe_filename(profile.name)}.yaml")
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(profile.to_dict(), f, default_flow_style=False)

    @classmethod
    def delete(cls, name: str) -> None:
        if name == "Default":
            return
        cls._profiles.pop(name, None)
        path = os.path.join(_PROFILES_DIR, f"{_safe_filename(name)}.yaml")
        if os.path.exists(path):
            os.remove(path)
        if cls._active_name == name:
            cls._active_name = "Default"
        if cls._default_name == name:
            cls._default_name = "Default"
            try:
                if os.path.exists(_DEFAULT_MARKER):
                    os.remove(_DEFAULT_MARKER)
            except OSError:
                pass

    @classmethod
    def duplicate(cls, source_name: str, new_name: str) -> ConversionProfile | None:
        source = cls._profiles.get(source_name)
        if not source:
            return None
        new_data = source.to_dict()
        new_data["name"] = new_name
        new_profile = ConversionProfile.from_dict(new_data)
        cls.save(new_profile)
        return new_profile

    @classmethod
    def rename(cls, old_name: str, new_name: str) -> None:
        if old_name == "Default" or old_name not in cls._profiles:
            return
        profile = cls._profiles.pop(old_name)
        old_path = os.path.join(_PROFILES_DIR, f"{_safe_filename(old_name)}.yaml")
        if os.path.exists(old_path):
            os.remove(old_path)
        profile.name = new_name
        cls.save(profile)
        if cls._active_name == old_name:
            cls._active_name = new_name
        if cls._default_name == old_name:
            cls._default_name = new_name
            try:
                with open(_DEFAULT_MARKER, "w", encoding="utf-8") as f:
                    f.write(new_name)
            except OSError:
                pass


def _safe_filename(name: str) -> str:
    return "".join(c if c.isalnum() or c in " -_" else "_" for c in name).strip()
