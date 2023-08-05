from pyocd.probe.aggregator import PROBE_CLASSES
from pyocd.probe.cmsis_dap_probe import CMSISDAPProbe
PROBE_CLASSES["cmsisdap"] = CMSISDAPProbe

from pyocd.__main__ import main
main()