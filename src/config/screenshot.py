# each tuple is (x, y, w, h) in % of the image
# w and h are hardcoded if not included in the tuple
SCREENSHOT_COORDS = {
    "16:9": {
        "quantity": (0.465, 0.89, 0.14, 0.06),
        "sort": (0.079, 0.9, 0.09, 0.033),
        "uid": (0.68958, 0.02129, 0.063, 0.02129),
        "character": {
            "count": (0.5525, 0.55, 0.0635, 0.0425),
            "chest": (0.44, 0.3315, 0.1245, 0.1037),
            "name": (0.0656, 0.059, 0.165, 0.0314),
            "level": (0.7975, 0.221, 0.02225, 0.031),
            "eidolons": [
                (0.3270416666666667, 0.17777777777777778),
                (0.5328125, 0.16574074074074074),
                (0.7802083333333333, 0.3574074074074074),
                (0.6661458333333333, 0.8074074074074075),
                (0.4171875, 0.7768518518518519),
                (0.184375, 0.6971481481481482),
            ],
            "traces": {
                "hunt": {
                    "basic": (0.502171875, 0.5347222222222222),
                    "skill": (0.65546875, 0.5347222222222222),
                    "ult": (0.579296875, 0.6006944444444444),
                    "talent": (0.579296875, 0.4615),
                },
                "erudition": {
                    "basic": (0.5076875, 0.5888888888888889),
                    "skill": (0.651171875, 0.5888888888888889),
                    "ult": (0.579296875, 0.5888888888888889),
                    "talent": (0.579296875, 0.4395833333333333),
                },
                "harmony": {
                    "basic": (0.508203125, 0.5493055555555556),
                    "skill": (0.6505625, 0.5493055555555556),
                    "ult": (0.579078125, 0.6458333333333334),
                    "talent": (0.579078125, 0.5243055555555556),
                },
                "preservation": {
                    "basic": (0.503515625, 0.6066388888888888),
                    "skill": (0.654125, 0.6069444444444444),
                    "ult": (0.5796875, 0.5881944444444445),
                    "talent": (0.5796875, 0.4615),
                },
                "destruction": {
                    "basic": (0.491796875, 0.56875),
                    "skill": (0.6640625, 0.56875),
                    "ult": (0.579734375, 0.5888888888888889),
                    "talent": (0.579734375, 0.4625),
                },
                "nihility": {
                    "basic": (0.498046875, 0.5173611111111112),
                    "skill": (0.658984375, 0.5173611111111112),
                    "ult": (0.579734375, 0.5048611111111111),
                    "talent": (0.579734375, 0.3875),
                },
                "abundance": {
                    "basic": (0.506640625, 0.5673611111111111),
                    "skill": (0.651953125, 0.5673611111111111),
                    "ult": (0.5796875, 0.59375),
                    "talent": (0.5796875, 0.4625),
                },
            },
        },
        # stats screenshot of selected item in inventory screen
        "stats": (0.72, 0.09, 0.25, 0.78),
        # (x0, y0, x1, y1) in % of the stats screenshot
        "light_cone": {
            "name": (0, 0, 1, 0.09),
            "level": (0.13, 0.32, 0.35, 0.37),
            "superimposition": (0.53, 0.495, 0.6, 0.55),
            "equipped": (0.45, 0.935, 0.67, 0.965),
            "equipped_avatar": (0.3525, 0.918, 0.4375, 0.966675),
            "lock": (0.896, 0.321, 0.97, 0.365),
        },
        "relic": {
            "name": (0, 0, 1, 0.09),
            "level": (0.115, 0.25, 0.23, 0.3),
            "discard": (0.865, 0.253, 0.935, 0.293),
            "lock": (0.865, 0.191, 0.935, 0.23),
            "rarity": (0.07, 0.15, 0.2, 0.22),
            "equipped": (0.45, 0.935, 0.67, 0.965),
            "equipped_avatar": (0.3525, 0.918, 0.4375, 0.966675),
            "mainStatKey": (0.11, 0.358, 0.7, 0.4),
            "substat_names": (0.11, 0.4, 0.5, 0.6),
            "substat_vals": (0.775, 0.4, 0.975, 0.6),
        },
    }
}
