from functions import validize_name
from prometheus_client import Gauge

BROMPTON_METRICS = {}
METRIC_PREFIX = "tessera_"

endpoints = [
    {"path": "input/active/refresh-rate", "description": "Active video input refresh rate", "type": "float", "range": "23.5 - 241.0"},
    {"path": "input/active/resolution/height", "description": "Active video input height", "type": "int", "range": "32 - 4096"},
    {"path": "input/active/resolution/width", "description": "Active video input width", "type": "int", "range": "32 - 4096"},
    {"path": "input/active/source/port-number", "description": "Which physical port instance is currently enabled for video input. For example, SDI A = port 1, SDI B = port 2. The available number of port instances for any port type will vary based on the processor hardware variant.", "type": "int", "range": "1 - 2"},
    {"path": "input/active/source/port-type", "description": "Which physical port instance is currently enabled for video input. The available types will vary based on the processor hardware variant.", "type": "enum", "supported_values": ["dvi", "hdmi", "sdi"]},
    {"path": "output/global-colour/brightness", "description": "Write -1 to reset output brightness to calculated common maximum for available fixtures.", "type": "float", "range": "-1 - 10000"},
    {"path": "output/global-colour/colour-temperature", "description": "Gets or sets the output colour temperature", "type": "float", "range": "2000 - 11000"},
    {"path": "output/global-colour/dark-magic/enabled", "description": "Enables or disables the processor's Dark Magic feature", "type": "bool"},
    {"path": "output/global-colour/gains/blue", "description": "Gets or sets the value of the output blue gain", "type": "float", "range": "0 - 100"},
    {"path": "output/global-colour/gains/green", "description": "Gets or sets the value of the output green gain", "type": "float", "range": "0 - 100"},
    {"path": "output/global-colour/gains/intensity", "description": "Gets or sets the value of the output intensity gain", "type": "float", "range": "0 - 100"},
    {"path": "output/global-colour/gains/red", "description": "Gets or sets the value of the output red gain", "type": "float", "range": "0 - 100"},
    {"path": "output/global-colour/gamma", "description": "Gets or sets the value of the output gamma", "type": "float", "range": "0.2 - 4.0"},
    {"path": "output/global-colour/puretone/enabled", "description": "Enables or disables PureTone", "type": "bool"},
    {"path": "output/network/failover/settings/enabled", "description": "Enables or disables failover mode on the processor", "type": "bool"},
    {"path": "output/network/failover/settings/modes/on-button-press", "description": "Enables or disables failover to backup processor when the processor's Blackout/Freeze buttons are pushed", "type": "bool"},
    {"path": "output/network/failover/settings/modes/on-partner-fail", "description": "Enables or disables partner processor failover when processor failure is detected (e.g. the processor loses power)", "type": "bool"},
    {"path": "output/network/failover/settings/modes/on-partner-video-fail", "description": "Enables or disables partner processor failover on video signal loss", "type": "bool"},
    {"path": "output/network/failover/settings/modes/prefer-primary", "description": "If prefer primary processor failover mode is activated, when primary processor is functioning correctly, it will be automatically always be the active processor", "type": "bool"},
    {"path": "output/network/failover/settings/role", "description": "Is processor's failover role Primary or Backup", "type": "enum", "supported_values": ["primary", "backup"]},
    {"path": "output/network/failover/state/is-active", "description": "Whether failover is active on the processor", "type": "bool"},
    {"path": "output/network/failover/state/is-partner-present", "description": "Whether the backup processor is currently online and detected", "type": "bool"},
    {"path": "output/network/failover/state/partner-absence-duration", "description": "How long the backup processor has been absent for", "type": "string"},
    {"path": "output/network/failover/state/partner-name", "description": "Name of the backup processor", "type": "string"},
    {"path": "output/network/failover/state/partner-serial", "description": "Serial number of the backup processor", "type": "string"},
    {"path": "output/network/failover/state/partner-video-absence-duration", "description": "Time since backup processor video source was last detected", "type": "string"},
    {"path": "override/blackout/enabled", "description": "Enables or disables blackout", "type": "bool"},
    {"path": "override/blackout/fade-time", "description": "The value of the blackout fade time. The fade time may be adjusted between zero (snap) and 10 seconds", "type": "float", "range": "0.0 - 10.0"},
    {"path": "override/freeze/enabled", "description": "Enables or disables video freeze", "type": "bool"},
    {"path": "override/test-pattern/enabled", "description": "Enables or disables test pattern output function", "type": "bool"},
    {"path": "override/test-pattern/format", "description": "Format of the generated test pattern", "type": "enum", "supported_values": ["from-input", "standard-dynamic-range", "perceptual-quantiser", "hybrid-log-gamma"]},
    {"path": "override/test-pattern/type", "description": "Determines which test pattern to generate. Defaults to SMPTE bars", "type": "enum", "supported_values": ["brompton", "brompton-overlay", "red", "green", "blue", "cyan", "magenta", "yellow", "white", "black", "grid", "scrollinggrid", "checkerboard", "scrolling-checkerboard", "colour-bars", "gamma", "gradient", "scrolling-gradient", "strobe", "smpte-bars", "scrolling-smpte-bars", "custom", "forty-five-degree-grid", "scrolling-forty-five-degree-grid"]},
    {"path": "panels/statistics/associated-count", "description": "The number of panels currently being controlled by the processor", "type": "int", "range": "0 - 2200"},
    {"path": "panels/statistics/error-count", "description": "The number of online panels currently reporting an error state", "type": "int", "range": "0 - 2048"},
    {"path": "panels/statistics/online-count", "description": "The number of online panels currently detected by the processor", "type": "int", "range": "0 - 2048"},
    {"path": "presets/active/name", "description": "Name of the currently active preset", "type": "string"},
    {"path": "presets/active/number", "description": "Set to activate a preset", "type": "string"},
    {"path": "processing/colour-correct/enabled", "description": "Enables or disables the processor's 14-Way Colour Correct feature", "type": "bool"},
    {"path": "processing/colour-replace/enabled", "description": "Enables or disables the processor's Colour Replace feature", "type": "bool"},
    {"path": "processing/curves/enabled", "description": "Enables or disables the processor's Colour Curves feature", "type": "bool"},
    {"path": "processing/osca/module-correction-enabled", "description": "Enables or disables OSCA module correction", "type": "bool"},
    {"path": "processing/osca/seam-correction-enabled", "description": "Enables or disables OSCA seam correction", "type": "bool"},
    {"path": "processing/scaler/enabled", "description": "Enables or disables scaler", "type": "bool"},
    {"path": "system/current-date-time", "description": "Current date/time of processor in yyyy-MM-dd hh:mm:ss 24 hour format", "type": "string"},
    {"path": "system/processor-type", "description": "Processor hardware model", "type": "enum", "supported_values": ["m2", "s4", "s8", "t1", "t8", "sx40"]},
    {"path": "system/software-version", "description": "Current version of software in format x.y.z", "type": "string"},
    {"path": "system/uptime", "description": "Time since processor boot in DDd HHh MMm SSs format", "type": "string"},
]

for endpoint in endpoints:
    description = endpoint['description']
    if 'range' in endpoint:
        description += f" RANGE: {endpoint['range']}"

    # Add the "source" label to the Gauge definition
    BROMPTON_METRICS[endpoint['path']] = Gauge(
        f"{METRIC_PREFIX}{validize_name(endpoint['path'])}",  # Add the prefix to the metric name
        description,  # Metric description
        ["source"]  # Label name for identifying sources
    )
