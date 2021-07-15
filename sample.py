import os

import idaapi

from sample import NAME
from sample.utils import debug, error, info


def load(plugin_name: str) -> None:
    """
    This reloads the plugin python package / modules.
    This is useful during plugin development
    """
    package_name = plugin_name.casefold()
    package_path = os.path.join(os.path.dirname(__file__), package_name)
    for entry in os.listdir(package_path):
        if not entry.endswith(".py"):
            continue

        module_name = entry[:-3]
        module_python_path = f"{package_name}.{module_name}"
        idaapi.require(module_python_path)


class Plugin(idaapi.plugin_t):
    NAME = NAME
    VERSION = "0.0.1"
    AUTHORS = f"The {NAME} team."

    flags = idaapi.PLUGIN_UNL
    comment = f"The {NAME} plugin."
    help = ""
    wanted_name = NAME
    wanted_hotkey = ""

    @staticmethod
    def description() -> str:
        return f"{Plugin.NAME} v{Plugin.VERSION}"

    def print_banner(self) -> None:
        description = f"{Plugin.NAME} v{Plugin.VERSION}"
        copyright = f"(c) {Plugin.AUTHORS}"
        info("-" * 80)
        info(f"{description} — {copyright}")
        info("-" * 80)

    def init(self):
        load(Plugin.NAME)
        debug("Init")
        try:
            # some initialization routines
            pass

        except Exception as err:
            error(str(err))
            return idaapi.PLUGIN_SKIP

        self.print_banner()
        return idaapi.PLUGIN_KEEP

    def run(self, arg):
        debug("Run")
        pass

    def term(self):
        debug("Term")
        pass


def PLUGIN_ENTRY():
    return Plugin()
