endpoints = [
    {
        "name": "DEVICE FIRMWARE",
        "path": "api/devices/items/{serial}/firmware",
        "description": "Current device firmware version",
        "type": "string"
    },
    {
        "name": "DEVICE TYPE",
        "path": "api/devices/items/{serial}/type",
        "description": "Device type name",
        "type": "string"
    },
    {
        "name": "ASSOCIATED DEVICES COUNT",
        "path": "api/devices/statistics/associated-count",
        "description": "The number of devices currently being controlled by the processor",
        "type": "int",
        "range": "0 - 2200"
    },
    {
        "name": "ERROR DEVICES COUNT",
        "path": "api/devices/statistics/error-count",
        "description": "The number of online devices currently reporting an error state",
        "type": "int",
        "range": "0 - 2048"
    },
    {
        "name": "ONLINE DEVICE COUNT",
        "path": "api/devices/statistics/online-count",
        "description": "The number of online devices currently detected by the processor",
        "type": "int",
        "range": "0 - 2048"
    },
    {
        "name": "GROUP BRIGHTNESS",
        "path": "api/groups/items/{number}/brightness",
        "description": "Gets or sets the group output brightness/luminance",
        "type": "int",
        "range": "0 - 10000"
    },
    {
        "name": "GROUP BRIGHTNESS LIMIT",
        "path": "api/groups/items/{number}/brightness-limit/enabled",
        "description": "Enables or disables group brightness limit",
        "type": "bool"
    },
    {
        "name": "GROUP BRIGHTNESS LIMIT VALUE",
        "path": "api/groups/items/{number}/brightness-limit/value",
        "description": "Current group maximum brightness value if brightness limit enabled",
        "type": "int",
        "range": "0 - 10000"
    },
    {
        "name": "GROUP COLOUR TEMPERATURE",
        "path": "api/groups/items/{number}/colour-temperature",
        "description": "Gets or sets the group colour temperature",
        "type": "int",
        "range": "2000 - 11000"
    },
    {
        "name": "GROUP DARK MAGIC ENABLED",
        "path": "api/groups/items/{number}/dark-magic/enabled",
        "description": "Enables or disables group Dark Magic",
        "type": "bool"
    },
    {
        "name": "GROUP EXTENDED BIT DEPTH",
        "path": "api/groups/items/{number}/extended-bit-depth/enabled",
        "description": "Enables or disables group extended bit depth",
        "type": "bool"
    },
    {
        "name": "GROUP BLUE GAIN",
        "path": "api/groups/items/{number}/gains/blue",
        "description": "Gets or sets the value of the group blue gain",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "GROUP GREEN GAIN",
        "path": "api/groups/items/{number}/gains/green",
        "description": "Gets or sets the value of the group green gain",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "GROUP INTENSITY GAIN",
        "path": "api/groups/items/{number}/gains/intensity",
        "description": "Gets or sets the value of the group intensity gain",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "GROUP RED GAIN",
        "path": "api/groups/items/{number}/gains/red",
        "description": "Gets or sets the value of the group red gain",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "GROUP OUTPUT GAMMA",
        "path": "api/groups/items/{number}/gamma",
        "description": "Gets or sets the group gamma value",
        "type": "float",
        "range": "0.2 - 4.0"
    },
    {
        "name": "GROUP GLOBAL COLOUR OVERRIDE",
        "path": "api/groups/items/{number}/global-colour-override",
        "description": "Enables or disables group global colour override",
        "type": "bool"
    },
    {
        "name": "GROUP GLOBAL GAINS OVERRIDE",
        "path": "api/groups/items/{number}/global-gains-override",
        "description": "Enables or disables group global gains override",
        "type": "bool"
    },
    {
        "name": "GROUP GLOBAL STARTRACKER OVERRIDE",
        "path": "api/groups/items/{number}/global-startracker-override",
        "description": "Enables or disables global StarTracker override for this group",
        "type": "bool"
    },
    {
        "name": "GROUP NAME",
        "path": "api/groups/items/{number}/name",
        "description": "Gets or sets the group name",
        "type": "string"
    },
    {
        "name": "GROUP OVERDRIVE ENABLED",
        "path": "api/groups/items/{number}/overdrive/enabled",
        "description": "Enables or disables group brightness overdrive",
        "type": "bool"
    },
    {
        "name": "GROUP PURE TONE ENABLED",
        "path": "api/groups/items/{number}/puretone/enabled",
        "description": "Enables or disables group PureTone",
        "type": "bool"
    },
    {
        "name": "GROUP STARTRACKER ENABLED",
        "path": "api/groups/items/{number}/startracker/enabled",
        "description": "Enables or disables markers in group StarTracker override",
        "type": "bool"
    },
    {
        "name": "INPUT PORT NUMBER",
        "path": "api/input/active/source/port-number",
        "description": "Which physical port instance is currently enabled for video input. For example, SDI A = port 1, SDI B",
        "type": "int",
        "range": "1 - 2"
    },
    {
        "name": "INPUT PORT TYPE",
        "path": "api/input/active/source/port-type",
        "description": "Which physical port instance is currently enabled for video input. The available types will vary based",
        "type": "enum",
        "supported_values": [
            "dvi",
            "hdmi",
            "sdi"
        ]
    },
    {
        "name": "DVI INPUT COLOUR SPACE",
        "path": "api/input/ports/dvi/{dvi-port-number}/controls/colour-space/colour",
        "description": "Gets or sets the colour space used for the incoming DVI content",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "INPUT DVI COLOUR FORMAT",
        "path": "api/input/ports/dvi/{dvi-port-number}/controls/dvi-colour-format",
        "description": "Gets or sets the colour format applied by the processor to the input for DVI input",
        "type": "enum",
        "supported_values": [
            "rgb",
            "ypbpr601",
            "ypbpr709"
        ]
    },
    {
        "name": "DVI DYNACAL BLUE GAMUT",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/blue/gamut",
        "description": "Blue component of DVI input colour space",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "DVI DYNACAL BLUE X",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/blue/x",
        "description": "Blue component X value of DVI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "DVI DYNACAL BLUE Y",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/blue/y",
        "description": "DVI component Y value of video input colour space",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "DVI DYNACAL GREEN GAMUT",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/green/gamut",
        "description": "Green component of DVI input colour space",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "DVI DYNACAL GREEN X",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/green/x",
        "description": "Green component X value of DVI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "DVI DYNACAL GREEN Y",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/green/y",
        "description": "Green component Y value of DVI input colour space",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "DVI DYNACAL RED GAMUT",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/red/gamut",
        "description": "Red component of DVI input colour space",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "DVI DYNACAL RED X",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/red/x",
        "description": "Red component X value of DVI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "DVI DYNACAL RED Y",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/red/y",
        "description": "Red component Y value of DVI input colour space",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "DVI DYNACAL WHITE COLOUR TEMPERATURE",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/white/colour-temperature",
        "description": "DVI input white component colour temperature",
        "type": "int",
        "range": "2000 - 11000"
    },
    {
        "name": "DVI DYNACAL WHITE GAMUT",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/white/gamut",
        "description": "White component of DVI input colour space. Set to 'Colour Temperature' to control this white-only",
        "type": "enum",
        "supported_values": [
            "d65",
            "aces",
            "colour-temperature",
            "custom"
        ]
    },
    {
        "name": "DVI DYNACAL WHITE X",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/white/x",
        "description": "White component X value of DVI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "DVI DYNACAL WHITE Y",
        "path": "api/input/ports/dvi/{dvi-port-number}/dynacal/white/y",
        "description": "DVI input white component Y value",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "DVI INPUT REFRESH RATE",
        "path": "api/input/ports/dvi/{dvi-port-number}/meta-data/refresh-rate",
        "description": "DVI input refresh rate",
        "type": "float",
        "range": "24 - 250"
    },
    {
        "name": "DVI INPUT RESOLUTION HEIGHT",
        "path": "api/input/ports/dvi/{dvi-port-number}/meta-data/resolution/height",
        "description": "DVI input height",
        "type": "int",
        "range": "32 - 4095"
    },
    {
        "name": "DVI INPUT RESOLUTION WIDTH",
        "path": "api/input/ports/dvi/{dvi-port-number}/meta-data/resolution/width",
        "description": "DVI input width",
        "type": "int",
        "range": "32 - 4096"
    },
    {
        "name": "DVI INPUT BLACK LEVEL",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/black-level",
        "description": "Gets or sets black level of a DVI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "DVI INPUT CONTRAST",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/contrast",
        "description": "Gets or sets contrast of a DVI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "DVI BLUE HIGHLIGHT",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/highlight/blue",
        "description": "Gets or sets blue highlight of a DVI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "DVI GREEN HIGHLIGHT",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/highlight/green",
        "description": "Gets or sets green highlight of a DVI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "DVI RED HIGHLIGHT",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/highlight/red",
        "description": "Gets or sets red highlight of a DVI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "DVI INPUT HUE",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/hue",
        "description": "Gets or sets hue of a DVI video input. 0\u00c3\u201a\u00c2\u00b0 is the passthough value",
        "type": "int",
        "range": "-180 - 180"
    },
    {
        "name": "DVI INPUT SATURATION",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/saturation",
        "description": "Gets or sets saturation of a DVI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "DVI BLUE SHADOW",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/shadow/blue",
        "description": "Gets or sets blue shadow of a DVI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "DVI GREEN SHADOW",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/shadow/green",
        "description": "Gets or sets green shadow of a DVI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "RED SHADOW",
        "path": "api/input/ports/dvi/{dvi-port-number}/proc-amp/shadow/red",
        "description": "Gets or sets red shadow of a DVI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "HDMI INPUT COLOUR SPACE",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/controls/colour-space/colour",
        "description": "Gets or sets the colour space used for the incoming HDMI content",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "INFOFRAME OVERRIDE ENABLED",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/controls/colour-space/info-frame-override-enabled",
        "description": "Enables or disables InfoFrame override",
        "type": "bool"
    },
    {
        "name": "HDMI INPUT COLOUR FORMAT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/controls/hdmi-colour-format",
        "description": "Gets or sets the colour format applied by the processor to the input for HDMI input",
        "type": "enum",
        "supported_values": [
            "from-input",
            "rgb",
            "ycbcr"
        ]
    },
    {
        "name": "HDMI INPUT HDR FORMAT OVERRIDE",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/controls/hdr/format",
        "description": "Gets or sets the HDR format applied by the processor to the input for HDMI input",
        "type": "enum",
        "supported_values": [
            "from-input",
            "standard-dynamic-range",
            "perceptual-quantiser",
            "hybrid-log-gamma"
        ]
    },
    {
        "name": "HDMI PQ AUTO BRIGHTEN",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/controls/hdr/pq/auto-brighten",
        "description": "Enables or disables PQ auto brighten for HDMI input",
        "type": "bool"
    },
    {
        "name": "HDMI PQ GAIN",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/controls/hdr/pq/gain",
        "description": "Gets or sets the value of the PQ gain for HDMI input",
        "type": "float",
        "range": "0.1 - 10.0"
    },
    {
        "name": "HDMI PQ MAXCLL OVERRIDE ENABLED",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/controls/hdr/pq/max-cll-override/enabled",
        "description": "Enables or disables PQ MaxCLL override for HDMI input",
        "type": "bool"
    },
    {
        "name": "HDMI PQ MAXCLL OVERRIDE LUMINANCE",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/controls/hdr/pq/max-cll-override/luminance",
        "description": "Gets or sets the value of the PQ MaxCLL override luminance for HDMI input",
        "type": "int",
        "range": "1 - 10000"
    },
    {
        "name": "HDMI INPUT QUANTISATION RANGE",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/controls/quantisation-range",
        "description": "Gets or sets the quantisation range applied by the processor to the HDMI input",
        "type": "enum",
        "supported_values": [
            "from-input",
            "full",
            "limited"
        ]
    },
    {
        "name": "HDMI DYNACAL BLUE GAMUT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/blue/gamut",
        "description": "Blue component of HDMI input colour space",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "HDMI DYNACAL BLUE X",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/blue/x",
        "description": "Blue component X value of HDMI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "HDMI DYNACAL BLUE Y",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/blue/y",
        "description": "Blue component Y value of HDMI input colour space",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "HDMI DYNACAL GREEN GAMUT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/green/gamut",
        "description": "Green component of HDMI input colour space",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "HDMI DYNACAL GREEN X",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/green/x",
        "description": "Green component X value of HDMI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "HDMI DYNACAL GREEN Y",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/green/y",
        "description": "Green component Y value of HDMI input colour space",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "HDMI DYNACAL RED GAMUT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/red/gamut",
        "description": "Red component of HDMI input colour space",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "HDMI DYNACAL RED X",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/red/x",
        "description": "Red component X value of HDMI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "HDMI DYNACAL RED Y",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/red/y",
        "description": "Red component Y value of HDMI input colour space",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "HDMI DYNACAL WHITE COLOUR TEMPERATURE",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/white/colour-temperature",
        "description": "HDMI input white component colour temperature",
        "type": "int",
        "range": "2000 - 11000"
    },
    {
        "name": "HDMI DYNACAL WHITE GAMUT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/white/gamut",
        "description": "White component of HDMI input colour space. Set to 'Colour Temperature' to control this white-only",
        "type": "enum",
        "supported_values": [
            "d65",
            "aces",
            "colour-temperature",
            "custom"
        ]
    },
    {
        "name": "HDMI DYNACAL WHITE X",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/white/x",
        "description": "White component X value of HDMI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "HDMI DYNACAL WHITE Y",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/dynacal/white/y",
        "description": "HDMI input white component Y value",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "HDMI INPUT BIT DEPTH",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/meta-data/bit-depth",
        "description": "Gets bit depth of HDMI video input. Valid values are 8, 10, and 12",
        "type": "int",
        "range": "8 - 12"
    },
    {
        "name": "HDMI INPUT HDR FORMAT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/meta-data/hdr/format",
        "description": "HDR format reported by the HDMI input",
        "type": "enum",
        "supported_values": [
            "standard-dynamic-range",
            "perceptual-quantiser",
            "hybrid-log-gamma"
        ]
    },
    {
        "name": "HDMI INPUT REFRESH RATE",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/meta-data/refresh-rate",
        "description": "Hdmi input refresh rate",
        "type": "float",
        "range": "24 - 250"
    },
    {
        "name": "HDMI INPUT RESOLUTION HEIGHT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/meta-data/resolution/height",
        "description": "HDMI input height",
        "type": "int",
        "range": "32 - 4095"
    },
    {
        "name": "HDMI INPUT RESOLUTION WIDTH",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/meta-data/resolution/width",
        "description": "HDMI input width",
        "type": "int",
        "range": "32 - 4096"
    },
    {
        "name": "HDMI INPUT SAMPLING",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/meta-data/sampling",
        "description": "Gets current HDMI sampling scheme",
        "type": "enum",
        "supported_values": [
            "rgb",
            "ycbcr422",
            "ycbcr444",
            "ycbcr420"
        ]
    },
    {
        "name": "HDMI INPUT BLACK LEVEL",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/black-level",
        "description": "Gets or sets black level of an HDMI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "HDMI INPUT CONTRAST",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/contrast",
        "description": "Gets or sets contrast of an HDMI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "HDMI BLUE HIGHLIGHT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/highlight/blue",
        "description": "Gets or sets blue highlight of an HDMI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "HDMI GREEN HIGHLIGHT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/highlight/green",
        "description": "Gets or sets green highlight of an HDMI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "HDMI RED HIGHLIGHT",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/highlight/red",
        "description": "Gets or sets red highlight of an HDMI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "HDMI INPUT HUE",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/hue",
        "description": "Gets or sets hue of an HDMI video input. 0\u00c3\u201a\u00c2\u00b0 is the passthough value",
        "type": "int",
        "range": "-180 - 180"
    },
    {
        "name": "HDMI INPUT SATURATION",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/saturation",
        "description": "Gets or sets saturation of an HDMI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "HDMI BLUE SHADOW",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/shadow/blue",
        "description": "Gets or sets blue shadow of an HDMI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "HDMI GREEN SHADOW",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/shadow/green",
        "description": "Gets or sets green shadow of an HDMI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "HDMI RED SHADOW",
        "path": "api/input/ports/hdmi/{hdmi-port-number}/proc-amp/shadow/red",
        "description": "Gets or sets red shadow of an HDMI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "SDI INPUT COLOUR SPACE",
        "path": "api/input/ports/sdi/{sdi-port-number}/controls/colour-space/colour",
        "description": "Gets or sets the colour space used for the incoming SDI content",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "SDI INPUT HDR FORMAT OVERRIDE",
        "path": "api/input/ports/sdi/{sdi-port-number}/controls/hdr/format",
        "description": "Gets or sets the HDR format applied by the processor to the input for SDI input",
        "type": "enum",
        "supported_values": [
            "from-input",
            "standard-dynamic-range",
            "perceptual-quantiser",
            "hybrid-log-gamma"
        ]
    },
    {
        "name": "SDI PQ AUTO BRIGHTEN",
        "path": "api/input/ports/sdi/{sdi-port-number}/controls/hdr/pq/auto-brighten",
        "description": "Enables or disables PQ auto brighten for SDI input",
        "type": "bool"
    },
    {
        "name": "SDI PQ GAIN",
        "path": "api/input/ports/sdi/{sdi-port-number}/controls/hdr/pq/gain",
        "description": "Gets or sets the value of the PQ gain for SDI input",
        "type": "float",
        "range": "0.1 - 10.0"
    },
    {
        "name": "SDI PQ MAXCLL OVERRIDE ENABLED",
        "path": "api/input/ports/sdi/{sdi-port-number}/controls/hdr/pq/max-cll-override/enabled",
        "description": "Enables or disables PQ MaxCLL override for SDI input",
        "type": "bool"
    },
    {
        "name": "SDI PQ MAXCLL OVERRIDE LUMINANCE",
        "path": "api/input/ports/sdi/{sdi-port-number}/controls/hdr/pq/max-cll-override/luminance",
        "description": "Gets or sets the value of the PQ MaxCLL override luminance for SDI input",
        "type": "int",
        "range": "1 - 10000"
    },
    {
        "name": "SDI DYNACAL BLUE GAMUT",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/blue/gamut",
        "description": "Blue component of SDI input colour space",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "SDI DYNACAL BLUE X",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/blue/x",
        "description": "Blue component X value of SDI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "SDI DYNACAL BLUE Y",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/blue/y",
        "description": "Blue component Y value of SDI input colour space",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "SDI DYNACAL GREEN GAMUT",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/green/gamut",
        "description": "Green component of SDI input colour space",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "SDI DYNACAL GREEN X",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/green/x",
        "description": "Green component X value of SDI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "SDI DYNACAL GREEN Y",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/green/y",
        "description": "Green component Y value of SDI input colour space",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "SDI DYNACAL RED GAMUT",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/red/gamut",
        "description": "Red component of SDI input colour space",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "SDI DYNACAL RED X",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/red/x",
        "description": "Red component X value of SDI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "SDI DYNACAL RED Y",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/red/y",
        "description": "Red component Y value of SDI input colour space",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "SDI DYNACAL WHITE COLOUR TEMPERATURE",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/white/colour-temperature",
        "description": "SDI input white component colour temperature",
        "type": "int",
        "range": "2000 - 11000"
    },
    {
        "name": "SDI DYNACAL WHITE GAMUT",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/white/gamut",
        "description": "White component of SDI input colour space. Set to 'Colour Temperature' to control this white-only",
        "type": "enum",
        "supported_values": [
            "d65",
            "aces",
            "colour-temperature",
            "custom"
        ]
    },
    {
        "name": "SDI DYNACAL WHITE X",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/white/x",
        "description": "White component X value of SDI input colour space",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "SDI DYNACAL WHITE Y",
        "path": "api/input/ports/sdi/{sdi-port-number}/dynacal/white/y",
        "description": "SDI input white component Y value",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "SDI INPUT REFRESH RATE",
        "path": "api/input/ports/sdi/{sdi-port-number}/meta-data/refresh-rate",
        "description": "SDI input refresh rate",
        "type": "float",
        "range": "24 - 250"
    },
    {
        "name": "SDI INPUT RESOLUTION HEIGHT",
        "path": "api/input/ports/sdi/{sdi-port-number}/meta-data/resolution/height",
        "description": "SDI input height",
        "type": "int",
        "range": "32 - 4095"
    },
    {
        "name": "SDI INPUT RESOLUTION WIDTH",
        "path": "api/input/ports/sdi/{sdi-port-number}/meta-data/resolution/width",
        "description": "SDI input width",
        "type": "int",
        "range": "32 - 4096"
    },
    {
        "name": "SDI INPUT BLACK LEVEL",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/black-level",
        "description": "Gets or sets black level of an SDI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "SDI INPUT CONTRAST",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/contrast",
        "description": "Gets or sets contrast of an SDI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "SDI BLUE HIGHLIGHT",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/highlight/blue",
        "description": "Gets or sets blue highlight of an SDI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "SDI GREEN HIGHLIGHT",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/highlight/green",
        "description": "Gets or sets green highlight of an SDI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "SDI RED HIGHLIGHT",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/highlight/red",
        "description": "Gets or sets red highlight of an SDI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "SDI INPUT HUE",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/hue",
        "description": "Gets or sets hue of an SDI video input. 0\u00c3\u201a\u00c2\u00b0 is the passthough value",
        "type": "int",
        "range": "-180 - 180"
    },
    {
        "name": "SDI INPUT SATURATION",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/saturation",
        "description": "Gets or sets saturation of an SDI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "SDI BLUE SHADOW",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/shadow/blue",
        "description": "Gets or sets blue shadow of an SDI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "SDI GREEN SHADOW",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/shadow/green",
        "description": "Gets or sets green shadow of an SDI input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "SDI RED SHADOW",
        "path": "api/input/ports/sdi/{sdi-port-number}/proc-amp/shadow/red",
        "description": "Gets or sets red shadow of an SDI video input. 100% is the passthough value",
        "type": "int",
        "range": "0 - 200"
    },
    {
        "name": "OUTPUT DYNACAL BLUE MODE",
        "path": "api/output/dynacal/{panel-type}/blue/mode",
        "description": "Gets or sets the blue component of panel output colour space",
        "type": "enum",
        "supported_values": [
            "achievable",
            "custom"
        ]
    },
    {
        "name": "OUTPUT DYNACAL BLUE X",
        "path": "api/output/dynacal/{panel-type}/blue/x",
        "description": "X value of panel output colour space blue component",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "OUTPUT DYNACAL BLUE Y",
        "path": "api/output/dynacal/{panel-type}/blue/y",
        "description": "Y value of panel output colour space blue component",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "OUTPUT DYNACAL GREEN MODE",
        "path": "api/output/dynacal/{panel-type}/green/mode",
        "description": "Gets or sets the green component of panel output colour space",
        "type": "enum",
        "supported_values": [
            "achievable",
            "custom"
        ]
    },
    {
        "name": "OUTPUT DYNACAL GREEN X",
        "path": "api/output/dynacal/{panel-type}/green/x",
        "description": "X value of panel output colour space green component",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "OUTPUT DYNACAL GREEN Y",
        "path": "api/output/dynacal/{panel-type}/green/y",
        "description": "Y value of panel output colour space green component",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "OUTPUT DYNACAL LUMINANCE ONLY FRACTION",
        "path": "api/output/dynacal/{panel-type}/luminance-only-fraction",
        "description": "Gets or sets the percentage mix of output calibration",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "OUTPUT DYNACAL MODE",
        "path": "api/output/dynacal/{panel-type}/mode",
        "description": "Gets or sets the panel output colour space",
        "type": "enum",
        "supported_values": [
            "match-input",
            "achievable",
            "custom"
        ]
    },
    {
        "name": "OUTPUT DYNACAL RED MODE",
        "path": "api/output/dynacal/{panel-type}/red/mode",
        "description": "Gets or sets the red component of panel output colour space",
        "type": "enum",
        "supported_values": [
            "achievable",
            "custom"
        ]
    },
    {
        "name": "OUTPUT DYNACAL RED X",
        "path": "api/output/dynacal/{panel-type}/red/x",
        "description": "X value of panel output colour space red component",
        "type": "float",
        "range": "0.0 - 0.8"
    },
    {
        "name": "OUTPUT DYNACAL RED Y",
        "path": "api/output/dynacal/{panel-type}/red/y",
        "description": "Y value of panel output colour space red component",
        "type": "float",
        "range": "0.0 - 0.9"
    },
    {
        "name": "OUTPUT BRIGHTNESS",
        "path": "api/output/global-colour/brightness",
        "description": "Write -1 to reset output brightness to calculated common maximum for available fixtures.",
        "type": "int",
        "range": "-1 - 10000"
    },
    {
        "name": "BRIGHTNESS LIMIT ENABLED",
        "path": "api/output/global-colour/brightness-limit/enabled",
        "description": "Enables or disables global brightness limit",
        "type": "bool"
    },
    {
        "name": "BRIGHTNESS LIMIT VALUE",
        "path": "api/output/global-colour/brightness-limit/value",
        "description": "Current maximum brightness value if brightness limit enabled",
        "type": "int",
        "range": "0 - 10000"
    },
    {
        "name": "OUTPUT COLOUR TEMPERATURE",
        "path": "api/output/global-colour/colour-temperature",
        "description": "Gets or sets the output colour temperature",
        "type": "int",
        "range": "2000 - 11000"
    },
    {
        "name": "DARK MAGIC ENABLED",
        "path": "api/output/global-colour/dark-magic/enabled",
        "description": "Enables or disables the processor's Dark Magic feature",
        "type": "bool"
    },
    {
        "name": "HIGHLIGHT OUT OF GAMUT PIXELS ENABLED",
        "path": "api/output/global-colour/dynacal/highlight-out-of-gamut-pixels-enabled",
        "description": "Enables or disables DynaCal's out-of-gamut pixel feature",
        "type": "bool"
    },
    {
        "name": "HIGHLIGHT OVERBRIGHT PIXELS ENABLED",
        "path": "api/output/global-colour/dynacal/highlight-overbright-pixels-enabled",
        "description": "Enables or disables DynaCal's overbright pixel feature",
        "type": "bool"
    },
    {
        "name": "EXTENDED BIT DEPTH ENABLED",
        "path": "api/output/global-colour/extended-bit-depth/enabled",
        "description": "Enables or disables extended bit depth",
        "type": "bool"
    },
    {
        "name": "BLUE GAIN",
        "path": "api/output/global-colour/gains/blue",
        "description": "Gets or sets the value of the output blue gain",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "GREEN GAIN",
        "path": "api/output/global-colour/gains/green",
        "description": "Gets or sets the value of the output green gain",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "INTENSITY GAIN",
        "path": "api/output/global-colour/gains/intensity",
        "description": "Gets or sets the value of the output intensity gain",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "RED GAIN",
        "path": "api/output/global-colour/gains/red",
        "description": "Gets or sets the value of the output red gain",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "OUTPUT GAMMA",
        "path": "api/output/global-colour/gamma",
        "description": "Gets or sets the value of the output gamma",
        "type": "float",
        "range": "0.2 - 4.0"
    },
    {
        "name": "OVERDRIVE ENABLED",
        "path": "api/output/global-colour/overdrive/enabled",
        "description": "Enables or disables global brightness overdrive",
        "type": "bool"
    },
    {
        "name": "PURE TONE ENABLED",
        "path": "api/output/global-colour/puretone/enabled",
        "description": "Enables or disables PureTone",
        "type": "bool"
    },
    {
        "name": "NETWORK BIT DEPTH",
        "path": "api/output/network/bit-depth",
        "description": "Gets or sets bit depth of video output. Valid values are 8, 10, and 12",
        "type": "int",
        "range": "8 - 12"
    },
    {
        "name": "REDUNDANT CABLE LOOP STATE",
        "path": "api/output/network/cable-redundancy/loops/{loop-number}/state",
        "description": "Current state of cable loop redundancy on the processor in the format : ->, where can be: 'loopfound',",
        "type": "string"
    },
    {
        "name": "REQUEST FAILOVER",
        "path": "api/output/network/failover/actions/request-failover",
        "description": "Send an empty string to activate processor redundancy",
        "type": "string"
    },
    {
        "name": "FAILOVER ENABLED",
        "path": "api/output/network/failover/settings/enabled",
        "description": "Enables or disables failover mode on the processor",
        "type": "bool"
    },
    {
        "name": "BUTTON PRESS FAILOVER MODE ENABLED",
        "path": "api/output/network/failover/settings/modes/on-button-press",
        "description": "Enables or disables failover to backup processor when the processor's Blackout/Freeze buttons are",
        "type": "bool"
    },
    {
        "name": "PARTNER FAILOVER MODE ENABLED",
        "path": "api/output/network/failover/settings/modes/on-partner-fail",
        "description": "Enables or disables partner processor failover when processor failure is detected (e.g. the processor",
        "type": "bool"
    },
    {
        "name": "PARTNER VIDEO FAILOVER MODE ENABLED",
        "path": "api/output/network/failover/settings/modes/on-partner-video-fail",
        "description": "Enables or disables partner processor failover on video signal loss",
        "type": "bool"
    },
    {
        "name": "PREFER PRIMARY FAILOVER MODE ENABLED",
        "path": "api/output/network/failover/settings/modes/prefer-primary",
        "description": "If prefer primary processor failover mode is activated, when primary processor is functioning",
        "type": "bool"
    },
    {
        "name": "FAILOVER ROLE",
        "path": "api/output/network/failover/settings/role",
        "description": "Is processor's failover role Primary or Backup",
        "type": "enum",
        "supported_values": [
            "primary",
            "backup"
        ]
    },
    {
        "name": "FAILOVER IS ACTIVE",
        "path": "api/output/network/failover/state/is-active",
        "description": "Whether failover is active on the processor",
        "type": "bool"
    },
    {
        "name": "FAILOVER PARTNER IS ONLINE",
        "path": "api/output/network/failover/state/is-partner-present",
        "description": "Whether the backup processor is currently online and detected",
        "type": "bool"
    },
    {
        "name": "FAILOVER PARTNER ABSENCE DURATION",
        "path": "api/output/network/failover/state/partner-absence-duration",
        "description": "How long the backup processor has been absent for",
        "type": "string"
    },
    {
        "name": "FAILOVER PARTNER NAME",
        "path": "api/output/network/failover/state/partner-name",
        "description": "Name of the backup processor",
        "type": "string"
    },
    {
        "name": "FAILOVER PARTNER SERIAL",
        "path": "api/output/network/failover/state/partner-serial",
        "description": "Serial number of the backup processor",
        "type": "string"
    },
    {
        "name": "FAILOVER PARTNER VIDEO ABSENCE DURATION",
        "path": "api/output/network/failover/state/partner-video-absence-duration",
        "description": "Time since backup processor video source was last detected",
        "type": "string"
    },
    {
        "name": "NETWORK FRAME RATE MULTIPLIER",
        "path": "api/output/network/frame-rate-multiplier",
        "description": "Gets or sets frame rate multiplier of video output. Set value to 1 to disable frame rate multiplication.",
        "type": "int",
        "range": "1 - 10"
    },
    {
        "name": "FRAME REMAPPING ENABLED",
        "path": "api/output/network/frame-remapping/enabled",
        "description": "Is frame remapping globally enabled or disabled",
        "type": "bool"
    },
    {
        "name": "FRAME REMAPPING BLUE",
        "path": "api/output/network/frame-remapping/frames/{frame}/blue",
        "description": "Gets or sets blue value of frame colour",
        "type": "int",
        "range": "0 - 255"
    },
    {
        "name": "FRAME REMAPPING GREEN",
        "path": "api/output/network/frame-remapping/frames/{frame}/green",
        "description": "Gets or sets green value of frame colour",
        "type": "int",
        "range": "0 - 255"
    },
    {
        "name": "FRAME REMAPPING MODE",
        "path": "api/output/network/frame-remapping/frames/{frame}/mode",
        "description": "Is frame mode Colour or Video",
        "type": "enum",
        "supported_values": [
            "colour",
            "video"
        ]
    },
    {
        "name": "FRAME REMAPPING RED",
        "path": "api/output/network/frame-remapping/frames/{frame}/red",
        "description": "Gets or sets red value of frame colour",
        "type": "int",
        "range": "0 - 255"
    },
    {
        "name": "FRAME REMAPPING X OFFSET",
        "path": "api/output/network/frame-remapping/frames/{frame}/x-offset",
        "description": "Gets or sets x offset of frame",
        "type": "int",
        "range": "-4095 - 4095"
    },
    {
        "name": "FRAME REMAPPING Y OFFSET",
        "path": "api/output/network/frame-remapping/frames/{frame}/y-offset",
        "description": "Gets or sets y offset of frame",
        "type": "int",
        "range": "-4095 - 4095"
    },
    {
        "name": "GENLOCKINTERNALSOURCERATE",
        "path": "api/output/network/genlock/internal-rate",
        "description": "Gets or sets current refresh rate for internal genlock source",
        "type": "float",
        "range": "23.5 - 251.0"
    },
    {
        "name": "GENLOCK PHASE OFFSET LINES",
        "path": "api/output/network/genlock/phase-offset/absolute/lines",
        "description": "Gets or sets genlock phase offset absolute lines value for the processor",
        "type": "int",
        "range": "-9999 - 9999"
    },
    {
        "name": "GENLOCK PHASE OFFSET PIXELS",
        "path": "api/output/network/genlock/phase-offset/absolute/pixels",
        "description": "Gets or sets genlock phase offset absolute pixels value for the processor",
        "type": "int",
        "range": "-9999 - 9999"
    },
    {
        "name": "GENLOCK PHASE OFFSET ANGLE",
        "path": "api/output/network/genlock/phase-offset/angle",
        "description": "Gets or sets genlock phase offset angle for the processor",
        "type": "float",
        "range": "-360 - 360"
    },
    {
        "name": "GENLOCK PHASE OFFSET FRACTION",
        "path": "api/output/network/genlock/phase-offset/fraction",
        "description": "Gets or sets genlock phase offset fraction for the processor",
        "type": "float",
        "range": "-100 - 100"
    },
    {
        "name": "GENLOCK PHASE OFFSET MODE",
        "path": "api/output/network/genlock/phase-offset/mode",
        "description": "Gets or sets genlock phase offset mode for the processor",
        "type": "enum",
        "supported_values": [
            "none",
            "angle",
            "fraction",
            "absolute"
        ]
    },
    {
        "name": "GENLOCK SOURCE",
        "path": "api/output/network/genlock/source",
        "description": "Gets or sets the current genlock source for the processor",
        "type": "enum",
        "supported_values": [
            "internal",
            "sdi",
            "sdi-a",
            "sdi-b",
            "hdmi",
            "dvi",
            "ref-in",
            "active-input"
        ]
    },
    {
        "name": "HIDDENMARKERS BACKGROUND GAIN",
        "path": "api/output/network/hidden-markers/background-gain",
        "description": "Gets or sets brightness of the video underneath hidden markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "HIDDENMARKERS BLACKOUT AFFECTS MARKERS",
        "path": "api/output/network/hidden-markers/blackout-affects-markers",
        "description": "Gets or sets whether blackout affects markers as well as video",
        "type": "bool"
    },
    {
        "name": "CLOSED SHUTTER MARKERS",
        "path": "api/output/network/hidden-markers/closed-shutter-markers",
        "description": "Gets or sets whether markers are only shown when camera shutter is closed",
        "type": "bool"
    },
    {
        "name": "CUSTOM MARKERS DATA",
        "path": "api/output/network/hidden-markers/custom/data",
        "description": "Send bulk data in image file format to upload custom markers",
        "type": "bytearray"
    },
    {
        "name": "CUSTOM MARKERS FILENAME",
        "path": "api/output/network/hidden-markers/custom/filename",
        "description": "The name of the stored custom markers file",
        "type": "string"
    },
    {
        "name": "CUSTOM MARKERS BLUE GAIN",
        "path": "api/output/network/hidden-markers/custom/marker-gain/blue",
        "description": "Gets or sets the current brightness of the blue custom markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "CUSTOM MARKERS GREEN GAIN",
        "path": "api/output/network/hidden-markers/custom/marker-gain/green",
        "description": "Gets or sets the current brightness of the green custom markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "CUSTOM MARKERS RED GAIN",
        "path": "api/output/network/hidden-markers/custom/marker-gain/red",
        "description": "Gets or sets the current brightness of the red custom markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "CUSTOM MARKERS SCALING",
        "path": "api/output/network/hidden-markers/custom/scaling",
        "description": "Gets or sets current scaling for hidden markers",
        "type": "enum",
        "supported_values": [
            "1:1",
            "stretch",
            "fit",
            "fill"
        ]
    },
    {
        "name": "HIDDENMARKERS ENABLED",
        "path": "api/output/network/hidden-markers/enabled",
        "description": "Enables or disables hidden markers",
        "type": "bool"
    },
    {
        "name": "HIDDENMARKERS FRAMES ENABLED ON",
        "path": "api/output/network/hidden-markers/frames-enabled-on",
        "description": "A valid array must contain ints in the range between 1 and the max supported frame rate multiplier",
        "type": "array"
    },
    {
        "name": "HIDDEN MARKERS MODE",
        "path": "api/output/network/hidden-markers/mode",
        "description": "Gets or sets current hidden markers mode",
        "type": "enum",
        "supported_values": [
            "none",
            "redspy",
            "startracker",
            "custom"
        ]
    },
    {
        "name": "REDSPY DISTANCE TO TRACKER",
        "path": "api/output/network/hidden-markers/redspy/distance-to-tracker",
        "description": "Gets or sets distance to tracker for RedSpy markers in metres",
        "type": "float",
        "range": "0.1 - 100.0"
    },
    {
        "name": "REDSPY MARKER GAIN",
        "path": "api/output/network/hidden-markers/redspy/marker-gain",
        "description": "Gets or sets the current brightness of the RedSpy markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "REDSPY MARKER SEED",
        "path": "api/output/network/hidden-markers/redspy/marker-seed",
        "description": "Gets or sets seed value for RedSpy marker positions",
        "type": "int",
        "range": "1 - 65535"
    },
    {
        "name": "REDSPY MARKER SIZE SCALER",
        "path": "api/output/network/hidden-markers/redspy/marker-size-scaler",
        "description": "Gets or sets the size scaling for RedSpy markers as a percentage",
        "type": "int",
        "range": "10 - 200"
    },
    {
        "name": "STARTRACKER BLUE DISTANCE TO TRACKER",
        "path": "api/output/network/hidden-markers/startracker/blue/distance-to-tracker",
        "description": "Gets or sets distance to tracker for blue StarTracker markers in metres",
        "type": "float",
        "range": "0.1 - 100.0"
    },
    {
        "name": "STARTRACKER BLUE ENABLED",
        "path": "api/output/network/hidden-markers/startracker/blue/enabled",
        "description": "Enables or disables blue markers for StarTracker",
        "type": "bool"
    },
    {
        "name": "STARTRACKER BLUE MARKER GAIN",
        "path": "api/output/network/hidden-markers/startracker/blue/marker-gain",
        "description": "Gets or sets the current brightness of the blue StarTracker markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "STARTRACKER BLUE MARKER SEED",
        "path": "api/output/network/hidden-markers/startracker/blue/marker-seed",
        "description": "Gets or sets seed value for blue StarTracker marker positions",
        "type": "int",
        "range": "1 - 65535"
    },
    {
        "name": "STARTRACKER BLUE MARKER SIZE SCALER",
        "path": "api/output/network/hidden-markers/startracker/blue/marker-size-scaler",
        "description": "Gets or sets the size scaling for blue StarTracker markers as a percentage",
        "type": "int",
        "range": "10 - 200"
    },
    {
        "name": "STARTRACKER GREEN DISTANCE TO TRACKER",
        "path": "api/output/network/hidden-markers/startracker/green/distance-to-tracker",
        "description": "Gets or sets distance to tracker for green StarTracker markers in metres",
        "type": "float",
        "range": "0.1 - 100.0"
    },
    {
        "name": "STARTRACKER GREEN ENABLED",
        "path": "api/output/network/hidden-markers/startracker/green/enabled",
        "description": "Enables or disables green markers for StarTracker",
        "type": "bool"
    },
    {
        "name": "STARTRACKER GREEN MARKER GAIN",
        "path": "api/output/network/hidden-markers/startracker/green/marker-gain",
        "description": "Gets or sets the current brightness of the green StarTracker markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "STARTRACKER GREEN MARKER SEED",
        "path": "api/output/network/hidden-markers/startracker/green/marker-seed",
        "description": "Gets or sets seed value for green StarTracker marker positions",
        "type": "int",
        "range": "1 - 65535"
    },
    {
        "name": "STARTRACKER GREEN MARKER SIZE SCALER",
        "path": "api/output/network/hidden-markers/startracker/green/marker-size-scaler",
        "description": "Gets or sets the size scaling for green StarTracker markers as a percentage",
        "type": "int",
        "range": "10 - 200"
    },
    {
        "name": "STARTRACKER RED DISTANCE TO TRACKER",
        "path": "api/output/network/hidden-markers/startracker/red/distance-to-tracker",
        "description": "Gets or sets distance to tracker for red StarTracker markers in metres",
        "type": "float",
        "range": "0.1 - 100.0"
    },
    {
        "name": "STARTRACKER RED ENABLED",
        "path": "api/output/network/hidden-markers/startracker/red/enabled",
        "description": "Enables or disables red markers for StarTracker",
        "type": "bool"
    },
    {
        "name": "STARTRACKER RED MARKER GAIN",
        "path": "api/output/network/hidden-markers/startracker/red/marker-gain",
        "description": "Gets or sets the current brightness of the red StarTracker markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "STARTRACKER RED MARKER SEED",
        "path": "api/output/network/hidden-markers/startracker/red/marker-seed",
        "description": "Gets or sets seed value for red StarTracker marker positions",
        "type": "int",
        "range": "1 - 65535"
    },
    {
        "name": "STARTRACKER RED MARKER SIZE SCALER",
        "path": "api/output/network/hidden-markers/startracker/red/marker-size-scaler",
        "description": "Gets or sets the size scaling for red StarTracker markers as a percentage",
        "type": "int",
        "range": "10 - 200"
    },
    {
        "name": "SHUTTERSYNC CUSTOM FRAME RATE",
        "path": "api/output/network/shuttersync/angle-settings/custom-frame-rate",
        "description": "Gets or sets the value of the ShutterSync custom frame rate",
        "type": "float",
        "range": "1 - 250"
    },
    {
        "name": "SHUTTERSYNC ANGLE",
        "path": "api/output/network/shuttersync/angle-settings/shutter-angle",
        "description": "Gets or sets the value of the shutter angle",
        "type": "float",
        "range": "1 - 360"
    },
    {
        "name": "SHUTTERSYNC USE CUSTOM FRAME RATE",
        "path": "api/output/network/shuttersync/angle-settings/use-custom-frame-rate",
        "description": "Enables or disables ShutterSync Custom Frame Rate",
        "type": "bool"
    },
    {
        "name": "SHUTTERSYNC DARK TIME",
        "path": "api/output/network/shuttersync/dark-time",
        "description": "Gets or sets the value of the ShutterSync dark time in milliseconds. Value stored independently of",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "SHUTTERSYNC DARK TIME MODE",
        "path": "api/output/network/shuttersync/dark-time-mode",
        "description": "Gets or sets the ShutterSync dark time mode. The processor can hold the dark time mode as a",
        "type": "enum",
        "supported_values": [
            "time",
            "percentage"
        ]
    },
    {
        "name": "SHUTTERSYNC DARK TIME PERCENTAGE",
        "path": "api/output/network/shuttersync/dark-time-percentage",
        "description": "Gets or sets the value of the ShutterSync dark time as a percentage of a frame. Value stored",
        "type": "float",
        "range": "0 - 100"
    },
    {
        "name": "SHUTTERSYNC INSERT DARK TIME",
        "path": "api/output/network/shuttersync/insert-dark-time",
        "description": "Enables or disables insertion of dark time. Inserting dark time corresponds to displaying black frames",
        "type": "bool"
    },
    {
        "name": "SHUTTERSYNC MODE",
        "path": "api/output/network/shuttersync/mode",
        "description": "Gets or sets ShutterSync operation mode",
        "type": "enum",
        "supported_values": [
            "none",
            "speed",
            "angle"
        ]
    },
    {
        "name": "SHUTTERSYNC PRIORITISE REFRESH RATE",
        "path": "api/output/network/shuttersync/prioritise-refresh-rate",
        "description": "Enables or disables ShutterSync prioritise refresh rate setting",
        "type": "bool"
    },
    {
        "name": "SHUTTERSYNC SENSOR READOUT TIME",
        "path": "api/output/network/shuttersync/sensor-readout-time",
        "description": "Gets or sets sensor readout time",
        "type": "float",
        "range": "0.00 - 42.00"
    },
    {
        "name": "SHUTTERSYNC SENSOR TYPE",
        "path": "api/output/network/shuttersync/sensor-type",
        "description": "Gets or sets ShutterSync sensor type",
        "type": "enum",
        "supported_values": [
            "any",
            "global-shutter",
            "rolling-shutter"
        ]
    },
    {
        "name": "SHUTTERSYNC SPEED",
        "path": "api/output/network/shuttersync/speed-settings/shutter-speed",
        "description": "Gets or sets the denominator value of ShutterSync speed, numerator is 1",
        "type": "float",
        "range": "10 - 250"
    },
    {
        "name": "SHUTTERSYNC TIME",
        "path": "api/output/network/shuttersync/speed-settings/time",
        "description": "Gets or sets the time value of ShutterSync speed",
        "type": "float",
        "range": "4 - 100"
    },
    {
        "name": "SHUTTERSYNC VIEWER",
        "path": "api/output/network/shuttersync/viewer",
        "description": "Gets or sets the ShutterSync viewer mode",
        "type": "enum",
        "supported_values": [
            "eye",
            "camera"
        ]
    },
    {
        "name": "OLD STARTRACKER BACKGROUND GAIN",
        "path": "api/output/network/startracker/background-gain",
        "description": "Gets or sets brightness of the video underneath StarTracker markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "OLD STARTRACKER BLACKOUT AFFECTS MARKERS",
        "path": "api/output/network/startracker/blackout-affects-markers",
        "description": "Gets or sets whether blackout affects markers as well as video",
        "type": "bool"
    },
    {
        "name": "OLD STARTRACKER BLUE DISTANCE TO TRACKER",
        "path": "api/output/network/startracker/blue/distance-to-tracker",
        "description": "Gets or sets distance to tracker for blue StarTracker markers in metres",
        "type": "float",
        "range": "0.1 - 100.0"
    },
    {
        "name": "OLD STARTRACKER BLUE ENABLED",
        "path": "api/output/network/startracker/blue/enabled",
        "description": "Enables or disables blue markers for StarTracker",
        "type": "bool"
    },
    {
        "name": "OLD STARTRACKER BLUE MARKER GAIN",
        "path": "api/output/network/startracker/blue/marker-gain",
        "description": "Gets or sets the current brightness of the blue StarTracker markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "OLD STARTRACKER BLUE MARKER SIZE SCALER",
        "path": "api/output/network/startracker/blue/marker-size-scaler",
        "description": "Gets or sets the size scaling for blue StarTracker markers as a percentage",
        "type": "int",
        "range": "10 - 200"
    },
    {
        "name": "OLD STARTRACKER BLUE MARKER SEED",
        "path": "api/output/network/startracker/blue/star-map-seed",
        "description": "Gets or sets seed value for blue StarTracker marker positions",
        "type": "int",
        "range": "1 - 65535"
    },
    {
        "name": "OLD STARTRACKER ENABLED",
        "path": "api/output/network/startracker/enabled",
        "description": "Enables or disables StarTracker markers",
        "type": "bool"
    },
    {
        "name": "OLD STARTRACKER FRAMES ENABLED ON",
        "path": "api/output/network/startracker/frames-enabled-on",
        "description": "A valid array must contain ints in the range between 1 and the max supported frame rate multiplier",
        "type": "array"
    },
    {
        "name": "OLD STARTRACKER GREEN DISTANCE TO TRACKER",
        "path": "api/output/network/startracker/green/distance-to-tracker",
        "description": "Gets or sets distance to tracker for green StarTracker markers in metres",
        "type": "float",
        "range": "0.1 - 100.0"
    },
    {
        "name": "OLD STARTRACKER GREEN ENABLED",
        "path": "api/output/network/startracker/green/enabled",
        "description": "Enables or disables green markers for StarTracker",
        "type": "bool"
    },
    {
        "name": "OLD STARTRACKER GREEN MARKER GAIN",
        "path": "api/output/network/startracker/green/marker-gain",
        "description": "Gets or sets the current brightness of the green StarTracker markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "OLD STARTRACKER GREEN MARKER SIZE SCALER",
        "path": "api/output/network/startracker/green/marker-size-scaler",
        "description": "Gets or sets the size scaling for green StarTracker markers as a percentage",
        "type": "int",
        "range": "10 - 200"
    },
    {
        "name": "OLD STARTRACKER GREEN MARKER SEED",
        "path": "api/output/network/startracker/green/star-map-seed",
        "description": "Gets or sets seed value for green StarTracker marker positions",
        "type": "int",
        "range": "1 - 65535"
    },
    {
        "name": "OLD STARTRACKER RED DISTANCE TO TRACKER",
        "path": "api/output/network/startracker/red/distance-to-tracker",
        "description": "Gets or sets distance to tracker for red StarTracker markers in metres",
        "type": "float",
        "range": "0.1 - 100.0"
    },
    {
        "name": "OLD STARTRACKER RED ENABLED",
        "path": "api/output/network/startracker/red/enabled",
        "description": "Enables or disables red markers for StarTracker",
        "type": "bool"
    },
    {
        "name": "OLD STARTRACKER RED MARKER GAIN",
        "path": "api/output/network/startracker/red/marker-gain",
        "description": "Gets or sets the current brightness of the red StarTracker markers as a percentage",
        "type": "int",
        "range": "0 - 100"
    },
    {
        "name": "OLD STARTRACKER RED MARKER SIZE SCALER",
        "path": "api/output/network/startracker/red/marker-size-scaler",
        "description": "Gets or sets the size scaling for red StarTracker markers as a percentage",
        "type": "int",
        "range": "10 - 200"
    },
    {
        "name": "OLD STARTRACKER RED MARKER SEED",
        "path": "api/output/network/startracker/red/star-map-seed",
        "description": "Gets or sets seed value for red StarTracker marker positions",
        "type": "int",
        "range": "1 - 65535"
    },
    {
        "name": "BLACKOUT ENABLED",
        "path": "api/override/blackout/enabled",
        "description": "Enables or disables blackout",
        "type": "bool"
    },
    {
        "name": "BLACKOUT FADE TIME",
        "path": "api/override/blackout/fade-time",
        "description": "The value of the blackout fade time. The fade time may be adjusted between zero (snap) and 10",
        "type": "float",
        "range": "0.0 - 10.0"
    },
    {
        "name": "FREEZE ENABLED",
        "path": "api/override/freeze/enabled",
        "description": "Enables or disables video freeze",
        "type": "bool"
    },
    {
        "name": "TEST PATTERN CUSTOM COLOUR BLUE",
        "path": "api/override/test-pattern/custom-colour/blue",
        "description": "Gets or sets the custom colour test pattern blue value",
        "type": "int",
        "range": "0 - 4095"
    },
    {
        "name": "TEST PATTERN CUSTOM COLOUR GREEN",
        "path": "api/override/test-pattern/custom-colour/green",
        "description": "Gets or sets the custom colour test pattern green value",
        "type": "int",
        "range": "0 - 4095"
    },
    {
        "name": "TEST PATTERN CUSTOM COLOUR RED",
        "path": "api/override/test-pattern/custom-colour/red",
        "description": "Gets or sets the custom colour test pattern red value",
        "type": "int",
        "range": "0 - 4095"
    },
    {
        "name": "TEST PATTERN CUSTOM GRADIENT END BLUE",
        "path": "api/override/test-pattern/custom-gradient/end-colour/blue",
        "description": "Gets or sets blue component of custom gradient test pattern end colour as a 12 bit integer",
        "type": "int",
        "range": "0 - 4095"
    },
    {
        "name": "TEST PATTERN CUSTOM GRADIENT END GREEN",
        "path": "api/override/test-pattern/custom-gradient/end-colour/green",
        "description": "Gets or sets green component of custom gradient test pattern end colour as a 12 bit integer",
        "type": "int",
        "range": "0 - 4095"
    },
    {
        "name": "TEST PATTERN CUSTOM GRADIENT END RED",
        "path": "api/override/test-pattern/custom-gradient/end-colour/red",
        "description": "Gets or sets red component of custom gradient test pattern end colour as a 12 bit integer",
        "type": "int",
        "range": "0 - 4095"
    },
    {
        "name": "TEST PATTERN CUSTOM GRADIENT ORIENTATION",
        "path": "api/override/test-pattern/custom-gradient/orientation",
        "description": "Gets or sets the custom gradient test pattern orientation",
        "type": "enum",
        "supported_values": [
            "horizontal",
            "vertical"
        ]
    },
    {
        "name": "TEST PATTERN CUSTOM GRADIENT START GREEN",
        "path": "api/override/test-pattern/custom-gradient/start-colour/blue",
        "description": "Gets or sets green component of custom gradient test pattern start colour as a 12 bit integer",
        "type": "int",
        "range": "0 - 4095"
    },
    {
        "name": "TEST PATTERN CUSTOM GRADIENT START BLUE",
        "path": "api/override/test-pattern/custom-gradient/start-colour/green",
        "description": "Gets or sets blue component of custom gradient test pattern start colour as a 12 bit integer",
        "type": "int",
        "range": "0 - 4095"
    },
    {
        "name": "TEST PATTERN CUSTOM GRADIENT START RED",
        "path": "api/override/test-pattern/custom-gradient/start-colour/red",
        "description": "Gets or sets red component of custom gradient test pattern start colour as a 12 bit integer",
        "type": "int",
        "range": "0 - 4095"
    },
    {
        "name": "TEST PATTERN ENABLED",
        "path": "api/override/test-pattern/enabled",
        "description": "Enables or disables test pattern output function",
        "type": "bool"
    },
    {
        "name": "TEST PATTERN FORMAT",
        "path": "api/override/test-pattern/format",
        "description": "Format of the generated test pattern",
        "type": "enum",
        "supported_values": [
            "from-input",
            "standard-dynamic-range",
            "perceptual-quantiser",
            "hybrid-log-gamma"
        ]
    },
    {
        "name": "CAPTURE FRAME",
        "path": "api/override/test-pattern/frame-store/capture-frame",
        "description": "Captures the current frame and saves it to the frame store with the user number provided. (Warning:",
        "type": "int",
        "range": "1 - 50"
    },
    {
        "name": "DELETE FRAME",
        "path": "api/override/test-pattern/frame-store/delete-frame",
        "description": "Delete the frame store frame at the user number provided.",
        "type": "int",
        "range": "1 - 50"
    },
    {
        "name": "FRAME STORE COLOUR SPACE",
        "path": "api/override/test-pattern/frame-store/frames/{frame-user-number}/colour-space",
        "description": "Set colour space for the frame",
        "type": "enum",
        "supported_values": [
            "rec-2020",
            "dci-p3",
            "rec-709",
            "aces-cg",
            "custom"
        ]
    },
    {
        "name": "FRAME STORE ALPHA ENABLED",
        "path": "api/override/test-pattern/frame-store/frames/{frame-user-number}/enable-alpha",
        "description": "Set alpha mode for the frame",
        "type": "bool"
    },
    {
        "name": "FRAME STORE FORMAT",
        "path": "api/override/test-pattern/frame-store/frames/{frame-user-number}/format",
        "description": "Set format for the frame",
        "type": "enum",
        "supported_values": [
            "from-input",
            "standard-dynamic-range",
            "perceptual-quantiser",
            "hybrid-log-gamma"
        ]
    },
    {
        "name": "FRAME NAME",
        "path": "api/override/test-pattern/frame-store/frames/{frame-user-number}/name",
        "description": "Name of the Frame",
        "type": "string"
    },
    {
        "name": "FRAME STORE SCALING MODE",
        "path": "api/override/test-pattern/frame-store/frames/{frame-user-number}/scaling-mode",
        "description": "Set scaling mode for the frame",
        "type": "enum",
        "supported_values": [
            "1:1",
            "stretch",
            "fit",
            "fill"
        ]
    },
    {
        "name": "TEST PATTERN RESTRICT TO ACHIEVABLE COLOURS",
        "path": "api/override/test-pattern/restrict-to-achievable-colours",
        "description": "Enables or disables restrict to achievable colours switch",
        "type": "bool"
    },
    {
        "name": "TEST PATTERN TYPE",
        "path": "api/override/test-pattern/type",
        "description": "Determines which test pattern or frame store image will be shown when the test pattern widget is",
        "type": "enum",
        "range": "1 - 50",
        "supported_values": [
            "brompton",
            "red",
            "green",
            "blue",
            "cyan",
            "magenta",
            "yellow",
            "white",
            "black",
            "grid",
            "scrolling-grid",
            "checkerboard",
            "scrolling-checkerboard",
            "colour-bars",
            "scrolling-colour-bars",
            "gradient",
            "scrolling-gradient",
            "strobe",
            "smpte-bars",
            "scrolling-smpte-bars",
            "custom-colour",
            "custom",
            "forty-five-degree-grid",
            "scrolling-forty-five-degree-grid",
            "custom-gradient",
            "scrolling-custom-gradient"
        ]
    },
    {
        "name": "ACTIVE PRESET NAME",
        "path": "api/presets/active/name",
        "description": "Name of the currently active preset",
        "type": "string"
    },
    {
        "name": "ACTIVE PRESET NUMBER",
        "path": "api/presets/active/number",
        "description": "Set to activate a preset",
        "type": "int",
        "range": "1 - 128"
    },
    {
        "name": "PRESET NAME",
        "path": "api/presets/items/{number}/name",
        "description": "Processor preset name",
        "type": "string"
    },
    {
        "name": "PRESET STATUS",
        "path": "api/presets/items/{number}/status",
        "description": "Preset activation status",
        "type": "bool"
    },
    {
        "name": "PROCESSING",
        "path": "api/processing/colour-correct/yellow/saturation",
        "description": "Gets or sets the value of the yellow saturation",
        "type": "float",
        "range": "-100.0 - 100.0"
    },
    {
        "name": "COLOUR REPLACE APPLY TO BRIGHTNESS",
        "path": "api/processing/colour-replace/apply-to-brightness",
        "description": "Enables or disables apply to brightness switch for colour replace",
        "type": "bool"
    },
    {
        "name": "COLOUR REPLACE APPLY TO HUE",
        "path": "api/processing/colour-replace/apply-to-hue",
        "description": "Enables or disables apply to hue switch for colour replace",
        "type": "bool"
    },
    {
        "name": "COLOUR REPLACE APPLY TO SATURATION",
        "path": "api/processing/colour-replace/apply-to-saturation",
        "description": "Enables or disables apply to saturation switch for colour replace",
        "type": "bool"
    },
    {
        "name": "COLOUR REPLACE BRIGHTNESS TOLERANCE",
        "path": "api/processing/colour-replace/brightness-tolerance",
        "description": "Gets or sets the value of the brightness tolerance for colour replace",
        "type": "float",
        "range": "10.0 - 100.0"
    },
    {
        "name": "COLOUR REPLACE FROM BLUE",
        "path": "api/processing/colour-replace/colour-from/blue",
        "description": "Gets or sets the blue component of the colour replace source colour",
        "type": "int",
        "range": "0 - 255"
    },
    {
        "name": "COLOUR REPLACE FROM GREEN",
        "path": "api/processing/colour-replace/colour-from/green",
        "description": "Gets or sets the green component of the colour replace source colour",
        "type": "int",
        "range": "0 - 255"
    },
    {
        "name": "COLOUR REPLACE FROM RED",
        "path": "api/processing/colour-replace/colour-from/red",
        "description": "Gets or sets the red component of the colour replace source colour",
        "type": "int",
        "range": "0 - 255"
    },
    {
        "name": "COLOUR REPLACE TO BLUE",
        "path": "api/processing/colour-replace/colour-to/blue",
        "description": "Gets or sets the blue component of the colour replace target colour",
        "type": "int",
        "range": "0 - 255"
    },
    {
        "name": "COLOUR REPLACE TO GREEN",
        "path": "api/processing/colour-replace/colour-to/green",
        "description": "Gets or sets the green component of the colour replace target colour",
        "type": "int",
        "range": "0 - 255"
    },
    {
        "name": "COLOUR REPLACE TO RED",
        "path": "api/processing/colour-replace/colour-to/red",
        "description": "Gets or sets the red component of the colour replace target colour",
        "type": "int",
        "range": "0 - 255"
    },
    {
        "name": "COLOUR REPLACE COLOUR TOLERANCE",
        "path": "api/processing/colour-replace/colour-tolerance",
        "description": "Gets or sets the value of the colour tolerance for colour replace",
        "type": "float",
        "range": "10.0 - 100.0"
    },
    {
        "name": "COLOUR REPLACE ENABLED",
        "path": "api/processing/colour-replace/enabled",
        "description": "Enables or disables the processor's Colour Replace feature",
        "type": "bool"
    },
    {
        "name": "COLOUR REPLACE METHOD",
        "path": "api/processing/colour-replace/method",
        "description": "Gets or sets the method applied by the processor for colour replacement",
        "type": "enum",
        "supported_values": [
            "set-to-colour",
            "transform-to-colour"
        ]
    },
    {
        "name": "COLOUR REPLACE SOFTNESS",
        "path": "api/processing/colour-replace/softness",
        "description": "Gets or sets the value of the softness for colour replace",
        "type": "float",
        "range": "6.0 - 100.0"
    },
    {
        "name": "COLOUR REPLACE STRENGTH",
        "path": "api/processing/colour-replace/strength",
        "description": "Gets or sets the value of the strength for colour replace",
        "type": "float",
        "range": "6.0 - 100.0"
    },
    {
        "name": "COLOUR REPLACE VIEW MATTE",
        "path": "api/processing/colour-replace/view-matte",
        "description": "Enables or disables view matte for colour replace",
        "type": "bool"
    },
    {
        "name": "CURVES BLUE POINTS",
        "path": "api/processing/curves/blue/points",
        "description": "A valid array must contain JSON objects with x and y values specified in the range [0,1] e.g. [{x:0.2,",
        "type": "array"
    },
    {
        "name": "CURVES ENABLED",
        "path": "api/processing/curves/enabled",
        "description": "Enables or disables the processor's Colour Curves feature",
        "type": "bool"
    },
    {
        "name": "CURVES GREEN POINTS",
        "path": "api/processing/curves/green/points",
        "description": "A valid array must contain JSON objects with x and y values specified in the range [0,1] e.g. [{x:0.2,",
        "type": "array"
    },
    {
        "name": "CURVES RED POINTS",
        "path": "api/processing/curves/red/points",
        "description": "A valid array must contain JSON objects with x and y values specified in the range [0,1] e.g. [{x:0.2,",
        "type": "array"
    },
    {
        "name": "CURVES WHITE POINTS",
        "path": "api/processing/curves/white/points",
        "description": "A valid array must contain JSON objects with x and y values specified in the range [0,1] e.g. [{x:0.2,",
        "type": "array"
    },
    {
        "name": "OSCA MODULE CORRECTION ENABLED",
        "path": "api/processing/osca/module-correction-enabled",
        "description": "Enables or disables OSCA module correction",
        "type": "bool"
    },
    {
        "name": "OSCA SEAM CORRECTION ENABLED",
        "path": "api/processing/osca/seam-correction-enabled",
        "description": "Enables or disables OSCA seam correction",
        "type": "bool"
    },
    {
        "name": "SCALER",
        "path": "api/processing/scaler/enabled",
        "description": "Enables or disables scaler",
        "type": "bool"
    },
    {
        "name": "PROJECT NAME",
        "path": "api/project/name",
        "description": "Gets the name of the Project",
        "type": "string"
    },
    {
        "name": "SYSTEM REBOOT",
        "path": "api/system/actions/reboot",
        "description": "If the processor password is set then this must be sent in the body. Otherwise send a blank string to",
        "type": "string"
    },
    {
        "name": "SYSTEM SHUTDOWN",
        "path": "api/system/actions/shutdown",
        "description": "If the processor password is set then this must be sent in the body. Otherwise send a blank string to",
        "type": "string"
    },
    {
        "name": "CURRENT DATE AND TIME",
        "path": "api/system/fan/case/two/status",
        "description": "Current activation status of Case Fan 2",
        "type": "bool",
        "range": "0 - 5000"
    },
    {
        "name": "FPGA FAN SPEED",
        "path": "api/system/fan/fpga/speed",
        "description": "Current speed of the FPGA Fan. Supported only on SX40, S8.",
        "type": "float",
        "range": "0 - 5000"
    },
    {
        "name": "FPGA FAN STATUS",
        "path": "api/system/fan/fpga/status",
        "description": "Current activation status of the FPGA Fan. Supported only on SX40, S8.",
        "type": "bool"
    },
    {
        "name": "PROCESSOR NAME",
        "path": "api/system/processor-name",
        "description": "The name of the processor",
        "type": "string"
    },
    {
        "name": "PROCESSOR TYPE",
        "path": "api/system/processor-type",
        "description": "Processor hardware model",
        "type": "enum",
        "supported_values": [
            "m2",
            "s4",
            "s8",
            "t1",
            "t8",
            "sx40"
        ]
    },
    {
        "name": "SERIAL NUMBER",
        "path": "api/system/serial-number",
        "description": "Gets the Serial Number of the processor",
        "type": "string"
    },
    {
        "name": "SOFTWARE VERSION",
        "path": "api/system/software-version",
        "description": "Current version of software in format x.y.z",
        "type": "string"
    },
    {
        "name": "AMBIENT TEMPERATURE",
        "path": "api/system/temperature/ambient",
        "description": "Current Ambient Temperature. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "CPU TEMPERATURE",
        "path": "api/system/temperature/cpu",
        "description": "Current temperature of the main CPU core. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "DSP TEMPERATURE",
        "path": "api/system/temperature/dsp",
        "description": "Current Temperature of the DSP. Supported by M2, T1, S4.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "ETHERNET COPPER PHY A TEMPERATURE",
        "path": "api/system/temperature/ethernet/copper/a",
        "description": "Current Temperature of Ethernet Copper Physical Interface A. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "ETHERNET COPPER PHY B TEMPERATURE",
        "path": "api/system/temperature/ethernet/copper/b",
        "description": "Current Temperature of Ethernet Copper Physical Interface B. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "ETHERNET SFP A TEMPERATURE",
        "path": "api/system/temperature/ethernet/sfp/a",
        "description": "Current Temperature of Ethernet SFP A. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "ETHERNET SFP B TEMPERATURE",
        "path": "api/system/temperature/ethernet/sfp/b",
        "description": "Current Temperature of Ethernet SFP B. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "ETHERNET SFP C TEMPERATURE",
        "path": "api/system/temperature/ethernet/sfp/c",
        "description": "Current Temperature of Ethernet SFP C. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "ETHERNET SFP D TEMPERATURE",
        "path": "api/system/temperature/ethernet/sfp/d",
        "description": "Current Temperature of Ethernet SFP D. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "FPGA TEMPERATURE",
        "path": "api/system/temperature/fpga",
        "description": "Current temperature of the FPGA core. Supported by SX40, S8, M2.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "FRONT TEMPERATURE",
        "path": "api/system/temperature/front",
        "description": "Current Temperature of the Front Panel. Supported by M2.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "GPU TEMPERATURE",
        "path": "api/system/temperature/gpu",
        "description": "Current Temperature of the GPU. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "MAIN BOARD TEMPERATURE",
        "path": "api/system/temperature/main",
        "description": "Current Temperature of the Main Board. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "PSU TEMPERATURE",
        "path": "api/system/temperature/psu",
        "description": "Current Temperature of the PSU. Supported by SX40, S8.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "REAR TEMPERATURE",
        "path": "api/system/temperature/rear",
        "description": "Current Temperature of the Rear Panel. Supported by M2.",
        "type": "float",
        "range": "0 - 200"
    },
    {
        "name": "UPTIME",
        "path": "api/system/uptime",
        "description": "Time since processor boot in DDd HHh MMm SSs format",
        "type": "string"
    }
]
