"use strict";
(self.webpackChunkdfa_wargaming = self.webpackChunkdfa_wargaming || []).push([[833], {
    173(e, a, t) {
        t.r(a),
        t.d(a, {
            default: () => st
        });
        var n = t(9950)
          , s = t(8459)
          , r = t(2584)
          , i = t(7937)
          , l = t(3045)
          , o = t(6334)
          , m = t(6564)
          , c = (t(7382),
        t(6217));
        class u {
        }
        u.Data = {
            ammo: {
                name: "Ammo",
                fullname: "Ammo",
                tech: "Mixed",
                hasLoc: !0,
                omit: !1,
                subtypes: {
                    AC: "Autocannon",
                    Gauss: "Gauss",
                    HAG: "Hyper-Assault Gauss",
                    LBX: "LB-X AC",
                    MG: "Machine Gun",
                    RAC: "Rotary AC",
                    UAC: "Ultra AC",
                    ATM: "ATM",
                    LRM: "LRM",
                    LRT: "LRT",
                    SLRM: "Streak LRM",
                    MML: "MML",
                    MRM: "MRM",
                    SRM: "SRM",
                    SRT: "SRT",
                    SSRM: "Streak SRM",
                    Narc: "Narc",
                    ArrowIV: "Arrow IV",
                    Artillery: "Artillery",
                    Flamer: "Flamer",
                    TBolt: "Thunderbolt",
                    Bomb: "Bomb"
                }
            },
            ammolimited: {
                name: "Ammo",
                fullname: "Ammo (Limited)",
                tech: "Mixed",
                hasLoc: !0,
                omit: !1,
                isLimited: !0,
                subtypes: {
                    AC: "Autocannon",
                    Gauss: "Gauss",
                    HAG: "Hyper-Assault Gauss",
                    LBX: "LB-X AC",
                    MG: "Machine Gun",
                    RAC: "Rotary AC",
                    UAC: "Ultra AC",
                    ATM: "ATM",
                    LRM: "LRM",
                    LRT: "LRT",
                    SLRM: "Streak LRM",
                    MML: "MML",
                    MRM: "MRM",
                    SRM: "SRM",
                    SRT: "SRT",
                    SSRM: "Streak SRM",
                    Narc: "Narc",
                    ArrowIV: "Arrow IV",
                    Artillery: "Artillery",
                    Flamer: "Flamer",
                    TBolt: "Thunderbolt"
                }
            },
            case: {
                name: "CASE",
                fullname: "CASE",
                tech: "Mixed",
                hasLoc: !0,
                omit: !1
            },
            freecase: {
                name: "CASE",
                fullname: "Built-in CASE",
                tech: "Clan",
                hasLoc: !1,
                fixedLocation: "All",
                omit: !1
            },
            case2: {
                name: "CASE II",
                fullname: "CASE II",
                tech: "Mixed",
                hasLoc: !0,
                omit: !1
            },
            ams: {
                name: "AMS",
                fullname: "Anti-Missile System",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            lams: {
                name: "LAMS",
                fullname: "Laser AMS",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            aiv: {
                name: "Artemis IV",
                fullname: "Artemis IV FCS",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            av: {
                name: "Artemis V",
                fullname: "Artemis V FCS",
                tech: "Clan",
                hasLoc: !1,
                omit: !1
            },
            apollo: {
                name: "Apollo FCS",
                fullname: "Apollo FCS",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            probe: {
                name: "Beagle Probe",
                fullname: "Beagle Active Probe",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            bhprobe: {
                name: "Bloodhound Probe",
                fullname: "Bloodhound Active Probe",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            cprobe: {
                name: "Active Probe",
                fullname: "Active Probe",
                tech: "Clan",
                hasLoc: !1,
                omit: !1
            },
            lprobe: {
                name: "Light Probe",
                fullname: "Light Active Probe",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            clprobe: {
                name: "Light Probe",
                fullname: "Light Active Probe",
                tech: "Clan",
                hasLoc: !1,
                omit: !1
            },
            ecm: {
                name: "ECM",
                fullname: "Guardian ECM Suite",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            cecm: {
                name: "ECM",
                fullname: "ECM Suite",
                tech: "Clan",
                hasLoc: !1,
                omit: !1
            },
            aecm: {
                name: "Angel ECM",
                fullname: "Angel ECM Suite",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            cews: {
                name: "Active Probe, ECM",
                fullname: "Watchdog CEWS",
                tech: "Clan",
                hasLoc: !1,
                omit: !1
            },
            c3s: {
                name: "C3S",
                fullname: "C3 Slave Unit",
                tech: "IS",
                hasLoc: !0,
                omit: !1
            },
            c3m: {
                name: "C3M",
                fullname: "C3 Master Unit",
                tech: "IS",
                hasLoc: !0,
                omit: !1
            },
            c3bm: {
                name: "C3BM",
                fullname: "C3 Boosted Master Unit",
                tech: "IS",
                hasLoc: !0,
                omit: !1
            },
            c3bs: {
                name: "C3BS",
                fullname: "C3 Boosted Slave Unit",
                tech: "IS",
                hasLoc: !0,
                omit: !1
            },
            c3i: {
                name: "C3i",
                fullname: "C3 Computer (Improved)",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            tag: {
                name: "TAG",
                fullname: "Target Acquistion Gear",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            ltag: {
                name: "L-TAG",
                fullname: "Light Target Acquistion Gear",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            tc: {
                name: "Targeting Computer",
                fullname: "Targeting Computer",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            jump: {
                name: "Jump Jets",
                fullname: "Jump Jets",
                tech: "Mixed",
                hasLoc: !1,
                omit: !0
            },
            ijump: {
                name: "Improved Jump Jets",
                fullname: "Improved Jump Jets",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            mechjumpbooster: {
                name: "Jump Boosters",
                fullname: "Mechanical Jump Boosters",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            umu: {
                name: "UMU",
                fullname: "Underwater Maneuvering Unit",
                tech: "Mixed",
                hasLoc: !1,
                omit: !0
            },
            masc: {
                name: "MASC",
                fullname: "MASC",
                tech: "Mixed",
                hasLoc: !1,
                omit: !0
            },
            supercharger: {
                name: "Supercharger",
                fullname: "Supercharger",
                tech: "Mixed",
                hasLoc: !1,
                omit: !0
            },
            tsm: {
                name: "TSM",
                fullname: "Triple-Strength Myomer",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            aes: {
                name: "AES",
                fullname: "Acutator Enhancement System",
                tech: "Mixed",
                hasLoc: !0,
                omit: !1
            },
            partwing: {
                name: "Partial Wing",
                fullname: "Partial Wing",
                tech: "Mixed",
                hasLoc: !1,
                omit: !0
            },
            xle: {
                name: "XL Engine",
                fullname: "XL Fusion Engine",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            cxle: {
                name: "cXL Engine",
                fullname: "XL Fusion Engine",
                tech: "Clan",
                hasLoc: !1,
                omit: !1
            },
            xxle: {
                name: "XXL Engine",
                fullname: "XXL Fusion Engine",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            cxxle: {
                name: "cXXL Engine",
                fullname: "XXL Fusion Engine",
                tech: "Clan",
                hasLoc: !1,
                omit: !1
            },
            lfe: {
                name: "Light Engine",
                fullname: "Light Fusion Engine",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            hdgyro: {
                name: "HD Gyro",
                fullname: "Heavy-Duty Gyro",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            lasrefl: {
                name: "Reflective Armor",
                fullname: "Laser-Reflective Armor",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            reactive: {
                name: "Reactive Armor",
                fullname: "Reactive Armor",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            ballreinf: {
                name: "Ballistic-Reinforced Armor",
                fullname: "Ballistic-Reinforced Armor",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            stealth: {
                name: "Stealth Armor",
                fullname: "Stealth Armor",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            hardened: {
                name: "Hardened Armor",
                fullname: "Hardened Armor",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            ferolam: {
                name: "Ferro-Lam Armor",
                fullname: "Ferro-Lamellor Armor",
                tech: "Clan",
                hasLoc: !1,
                omit: !1
            },
            composite: {
                name: "Composite Structure",
                fullname: "Composite Structure",
                tech: "IS",
                hasLoc: !1,
                omit: !0
            },
            reinforced: {
                name: "Reinforced Structure",
                fullname: "Reinforced Structure",
                tech: "Mixed",
                hasLoc: !1,
                omit: !0
            },
            ppccapacitor: {
                name: "PPC Capacitor",
                fullname: "PPC Capacitor",
                tech: "Mixed",
                hasLoc: !0,
                omit: !1
            },
            armcomp: {
                name: "Armored Components",
                fullname: "Armored Components",
                tech: "Mixed",
                hasLoc: !0,
                omit: !1
            },
            smcp: {
                name: "Small Cockpit",
                fullname: "Small Cockpit",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            tmcp: {
                name: "Torso Cockpit",
                fullname: "Torso-Mounted Cockpit",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            cpod: {
                name: "Coolant Pods",
                fullname: "Coolant Pods",
                tech: "Mixed",
                hasLoc: !1,
                isLimited: !0,
                omit: !0
            },
            apod: {
                name: "A-Pods",
                fullname: "Anti-Personnel Pods",
                tech: "Mixed",
                hasLoc: !1,
                isLimited: !0,
                omit: !1
            },
            bpod: {
                name: "B-Pods",
                fullname: "Anti-Battle Armor Pods",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            mpod: {
                name: "M-Pods",
                fullname: "Anti-BattleMech Pods",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            turret: {
                name: "Turret",
                fullname: "Turret",
                tech: "Mixed",
                hasLoc: !0,
                omit: !1
            },
            troopspace: {
                name: "IT",
                fullname: "Infantry Transport (Tons)",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1,
                isLimited: !0
            },
            bafireresist: {
                name: "Fire Resistant Armor",
                fullname: "BA Fire Resistant Armor",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            bamimetic: {
                name: "Mimetic Armor",
                fullname: "BA Mimetic Armor",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            bareactive: {
                name: "Reactive Armor",
                fullname: "BA Reactive Armor",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            bareflective: {
                name: "Reflective Armor",
                fullname: "BA Reflective Armor",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            bastealth: {
                name: "Stealth Armor",
                fullname: "BA Stealth Armor",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            jumpbooster: {
                name: "Jump Booster",
                fullname: "Jump Booster",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            apds: {
                name: "APDS",
                fullname: "Advanced Point Defense System",
                tech: "IS",
                hasLoc: !1,
                omit: !1
            },
            dwp: {
                name: "DWPs",
                fullname: "Detachable Weapon Pack(s)",
                tech: "Mixed",
                hasLoc: !1,
                omit: !1
            },
            myomerboost: {
                name: "Myomer Booster",
                fullname: "Myomer Booster",
                hasLoc: !1,
                omit: !1
            }
        };
        const h = u;
        const d = class {
            constructor(e) {
                this.id = e && e.id || "",
                this.location = this.hasLoc && e && e.location || "",
                this.subtype = e && e.subtype || "",
                this.uses = e && e.uses || ""
            }
            get name() {
                return this.id && h.Data[this.id].name || ""
            }
            get fullame() {
                return this.id && h.Data[this.id].fullame || ""
            }
            get tech() {
                return this.id && h.Data[this.id].tech || ""
            }
            get hasLoc() {
                return this.id && h.Data[this.id].hasLoc || !1
            }
            get subtypes() {
                return this.id && h.Data[this.id].subtypes
            }
            get isLimited() {
                return this.id && h.Data[this.id].isLimited || !1
            }
            get omit() {
                return this.id && h.Data[this.id].omit || !1
            }
            get fixedLocation() {
                return this.id && h.Data[this.id].fixedLocation ? h.Data[this.id].fixedLocation : ""
            }
            get location() {
                return this.fixedLocation ? this.fixedLocation : this._location || ""
            }
            set location(e) {
                this.fixedLocation || (this._location = e)
            }
            static sort(e, a) {
                let t = "ammo" === e.id
                  , n = "ammo" === a.id;
                return t && !n ? 1 : !t && n ? -1 : (t = e.name.toUpperCase(),
                n = a.name.toUpperCase(),
                t < n ? -1 : t > n ? 1 : 0)
            }
        }
        ;
        class g {
        }
        g.Data = {
            ac2: {
                name: "AC/2",
                fullname: "Autocannon/2",
                tech: "IS",
                type: "B",
                damage: "2",
                heat: "1",
                crits: "1",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useTC: "1",
                useAmmo: "AC"
            },
            ac5: {
                name: "AC/5",
                fullname: "Autocannon/5",
                tech: "IS",
                type: "B",
                damage: "5",
                heat: "1",
                crits: "4",
                rangePB: "2",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1",
                useAmmo: "AC"
            },
            ac10: {
                name: "AC/10",
                fullname: "Autocannon/10",
                tech: "IS",
                type: "B",
                damage: "10",
                heat: "3",
                crits: "7",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1",
                useAmmo: "AC"
            },
            ac20: {
                name: "AC/20",
                fullname: "Autocannon/20",
                tech: "IS",
                type: "B",
                damage: "20",
                heat: "7",
                crits: "10",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1",
                useAmmo: "AC"
            },
            lb2x: {
                name: "LB 2-X",
                fullname: "LB 2-X Autocannon",
                tech: "IS",
                type: "B",
                damage: "2",
                heat: "1",
                crits: "4",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "2",
                useTC: "1",
                useAmmo: "LBX"
            },
            lb5x: {
                name: "LB 5-X",
                fullname: "LB 5-X Autocannon",
                tech: "IS",
                type: "B",
                damage: "5",
                heat: "1",
                crits: "5",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useC: "1",
                useTC: "1",
                useAmmo: "LBX"
            },
            lb10x: {
                name: "LB 10-X",
                fullname: "LB 10-X Autocannon",
                tech: "IS",
                type: "B",
                damage: "10",
                heat: "2",
                crits: "6",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useC: "1",
                useTC: "1",
                useAmmo: "LBX"
            },
            lb20x: {
                name: "LB 20-X",
                fullname: "LB 20-X Autocannon",
                tech: "IS",
                type: "B",
                damage: "20",
                heat: "6",
                crits: "11",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useC: "1",
                useTC: "1",
                useAmmo: "LBX"
            },
            uac2: {
                name: "UAC/2",
                fullname: "Ultra Autocannon/2",
                tech: "IS",
                type: "B",
                damage: "2",
                heat: "1",
                crits: "3",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "2",
                useR: "2",
                useTC: "1",
                useAmmo: "UAC"
            },
            uac5: {
                name: "UAC/5",
                fullname: "Ultra Autocannon/5",
                tech: "IS",
                type: "B",
                damage: "5",
                heat: "1",
                crits: "5",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useR: "5",
                useTC: "1",
                useAmmo: "UAC"
            },
            uac10: {
                name: "UAC/10",
                fullname: "Ultra Autocannon/10",
                tech: "IS",
                type: "B",
                damage: "10",
                heat: "4",
                crits: "7",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useR: "10",
                useTC: "1",
                useAmmo: "UAC"
            },
            uac20: {
                name: "UAC/20",
                fullname: "Ultra Autocannon/20",
                tech: "IS",
                type: "B",
                damage: "20",
                heat: "8",
                crits: "10",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useR: "20",
                useTC: "1",
                useAmmo: "UAC"
            },
            rac2: {
                name: "RAC/2",
                fullname: "Rotary Autocannon/2",
                tech: "IS",
                type: "B",
                damage: "3",
                heat: "3",
                crits: "3",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useR: "6",
                useTC: "1",
                useAmmo: "RAC"
            },
            rac5: {
                name: "RAC/5",
                fullname: "Rotary Autocannon/5",
                tech: "IS",
                type: "B",
                damage: "8",
                heat: "3",
                crits: "6",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useR: "12",
                useTC: "1",
                useAmmo: "RAC"
            },
            hvac2: {
                name: "HVAC/2",
                fullname: "Hyper-Velocity Autocannon/2",
                tech: "IS",
                type: "B",
                damage: "2",
                heat: "1",
                crits: "2",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "0",
                rangeX: "2",
                useTC: "1",
                useAmmo: "AC"
            },
            hvac5: {
                name: "HVAC/5",
                fullname: "Hyper-Velocity Autocannon/5",
                tech: "IS",
                type: "B",
                damage: "5",
                heat: "3",
                crits: "4",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "2",
                useTC: "1",
                useAmmo: "AC"
            },
            hvac10: {
                name: "HVAC/10",
                fullname: "Hyper-Velocity Autocannon/10",
                tech: "IS",
                type: "B",
                damage: "10",
                heat: "7",
                crits: "6",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "4",
                useTC: "1",
                useAmmo: "AC"
            },
            lac2: {
                name: "LAC/2",
                fullname: "Light Autocannon/2",
                tech: "IS",
                type: "B",
                damage: "2",
                heat: "1",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1",
                useAmmo: "AC"
            },
            lac5: {
                name: "LAC/5",
                fullname: "Light Autocannnon/5",
                tech: "IS",
                type: "B",
                damage: "5",
                heat: "1",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1",
                useAmmo: "AC"
            },
            lgauss: {
                name: "LGauss",
                fullname: "Light Gauss Rifle",
                tech: "IS",
                type: "B",
                damage: "8",
                heat: "1",
                crits: "5",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "2",
                useTC: "1",
                useAmmo: "Gauss"
            },
            gauss: {
                name: "Gauss",
                fullname: "Gauss Rifle",
                tech: "IS",
                type: "B",
                damage: "15",
                heat: "1",
                crits: "7",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useTC: "1",
                useAmmo: "Gauss"
            },
            hgauss: {
                name: "HGauss",
                fullname: "Heavy Gauss Rifle",
                tech: "IS",
                type: "B",
                damage: "25",
                heat: "2",
                crits: "11",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                varPBSdamage: "25",
                varMdamage: "20",
                varLXdamage: "10",
                useTC: "1",
                useAmmo: "Gauss",
                specials: "var"
            },
            ihgauss: {
                name: "iHGauss",
                fullname: "Improved Heavy Gauss Rifle",
                tech: "IS",
                type: "B",
                damage: "22",
                heat: "2",
                crits: "11",
                rangePB: "2",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "4",
                useTC: "1",
                useAmmo: "Gauss"
            },
            magshot: {
                name: "MagShot",
                fullname: "MagShot",
                tech: "IS",
                type: "B",
                damage: "2",
                heat: "1",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1",
                useAmmo: "Gauss"
            },
            sbgauss: {
                name: "SBGauss",
                fullname: "Silver Bullet Gauss Rifle",
                tech: "IS",
                type: "B",
                damage: "15",
                heat: "1",
                crits: "7",
                rangePB: "2",
                rangeS: "-1",
                rangeM: "-1",
                rangeL: "1",
                rangeX: "3",
                useC: "1",
                useAmmo: "Gauss",
                specials: "sbg"
            },
            lmg: {
                name: "LMG",
                fullname: "Light Machine Gun",
                tech: "IS",
                type: "B",
                damage: "1",
                heat: "0",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "MG",
                specials: "ai"
            },
            mg: {
                name: "MG",
                fullname: "Machine Gun",
                tech: "IS",
                type: "B",
                damage: "2",
                heat: "0",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "MG",
                specials: "ai"
            },
            hmg: {
                name: "HMG",
                fullname: "Heavy Machine Gun",
                tech: "IS",
                type: "B",
                damage: "3",
                heat: "0",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "MG",
                specials: "ai"
            },
            nailrivet: {
                name: "NailRivet",
                fullname: "Nail/Rivet Gun",
                tech: "IS",
                type: "B",
                damage: "0",
                heat: "0",
                crits: "1",
                rangePB: "0",
                rangeS: "9",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: "ai"
            },
            slas: {
                name: "SLas",
                fullname: "Small Laser",
                tech: "Mixed",
                type: "E",
                damage: "3",
                heat: "1",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            mlas: {
                name: "MLas",
                fullname: "Medium Laser",
                tech: "IS",
                type: "E",
                damage: "5",
                heat: "3",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            llas: {
                name: "LLas",
                fullname: "Large Laser",
                tech: "IS",
                type: "E",
                damage: "8",
                heat: "8",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1"
            },
            ppc: {
                name: "PPC",
                fullname: "PPC",
                tech: "IS",
                type: "E",
                damage: "10",
                heat: "10",
                crits: "3",
                rangePB: "2",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1"
            },
            erslas: {
                name: "erSLas",
                fullname: "ER Small Laser",
                tech: "IS",
                type: "E",
                damage: "3",
                heat: "2",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            ermlas: {
                name: "erMLas",
                fullname: "ER Medium Laser",
                tech: "IS",
                type: "E",
                damage: "5",
                heat: "5",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1"
            },
            erllas: {
                name: "erLLas",
                fullname: "ER Large Laser",
                tech: "IS",
                type: "E",
                damage: "8",
                heat: "12",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useTC: "1"
            },
            erppc: {
                name: "erPPC",
                fullname: "ER PPC",
                tech: "IS",
                type: "E",
                damage: "10",
                heat: "15",
                crits: "3",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useTC: "1"
            },
            splas: {
                name: "SPLas",
                fullname: "Small Pulse Laser",
                tech: "IS",
                type: "E",
                damage: "3",
                heat: "2",
                crits: "1",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useTC: "1",
                specials: "ai"
            },
            mplas: {
                name: "MPLas",
                fullname: "Medium Pulse Laser",
                tech: "IS",
                type: "E",
                damage: "6",
                heat: "4",
                crits: "1",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            lplas: {
                name: "LPLas",
                fullname: "Large Pulse Laser",
                tech: "IS",
                type: "E",
                damage: "9",
                heat: "10",
                crits: "2",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "0",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            sxplas: {
                name: "SXPLas",
                fullname: "Small X-Pulse Laser",
                tech: "IS",
                type: "E",
                damage: "3",
                heat: "3",
                crits: "1",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1",
                specials: "ai"
            },
            mxplas: {
                name: "MXPLas",
                fullname: "Medium X-Pulse Laser",
                tech: "IS",
                type: "E",
                damage: "6",
                heat: "6",
                crits: "1",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "0",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            lxplas: {
                name: "LXPLas",
                fullname: "Large X-Pulse Laser",
                tech: "IS",
                type: "E",
                damage: "9",
                heat: "14",
                crits: "2",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "9",
                useTC: "1"
            },
            lppc: {
                name: "LPPC",
                fullname: "Light PPC",
                tech: "IS",
                type: "E",
                damage: "5",
                heat: "5",
                crits: "2",
                rangePB: "2",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1"
            },
            hppc: {
                name: "HPPC",
                fullname: "Heavy PPC",
                tech: "IS",
                type: "E",
                damage: "15",
                heat: "15",
                crits: "4",
                rangePB: "2",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1"
            },
            snppc: {
                name: "SNPPC",
                fullname: "Snub-Nose PPC",
                tech: "IS",
                type: "E",
                damage: "10",
                heat: "10",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "4",
                rangeX: "9",
                varPBSdamage: "10",
                varMdamage: "8",
                varLXdamage: "5",
                useTC: "1",
                specials: "var"
            },
            vssplas: {
                name: "vsSPLas",
                fullname: "Var Speed Small Pulse Laser",
                tech: "IS",
                type: "E",
                damage: "5",
                heat: "3",
                crits: "1",
                rangePB: "-3",
                rangeS: "-3",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                varPBSdamage: "5",
                varMdamage: "4",
                varLXdamage: "3",
                useTC: "1",
                specials: "var,ai"
            },
            vsmplas: {
                name: "vsMPLas",
                fullname: "Var Speed Medium Pulse Laser",
                tech: "IS",
                type: "E",
                damage: "9",
                heat: "7",
                crits: "2",
                rangePB: "-3",
                rangeS: "-3",
                rangeM: "0",
                rangeL: "9",
                rangeX: "9",
                varPBSdamage: "9",
                varMdamage: "7",
                varLXdamage: "5",
                useTC: "1",
                specials: "var"
            },
            vslplas: {
                name: "vsLPLas",
                fullname: "Var Speed Large Pulse Laser",
                tech: "IS",
                type: "E",
                damage: "11",
                heat: "10",
                crits: "4",
                rangePB: "-3",
                rangeS: "-3",
                rangeM: "0",
                rangeL: "3",
                rangeX: "9",
                varPBSdamage: "11",
                varMdamage: "9",
                varLXdamage: "7",
                useTC: "1",
                specials: "var"
            },
            reslas: {
                name: "reSLas",
                fullname: "Re-Engineered Small Laser",
                tech: "IS",
                type: "E",
                damage: "4",
                heat: "4",
                crits: "1",
                rangePB: "-1",
                rangeS: "-1",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            remlas: {
                name: "reMLas",
                fullname: "Re-Engineered Medium Laser",
                tech: "IS",
                type: "E",
                damage: "6",
                heat: "6",
                crits: "2",
                rangePB: "-1",
                rangeS: "-1",
                rangeM: "1",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            rellas: {
                name: "reLLas",
                fullname: "Re-Engineered Large Laser",
                tech: "IS",
                type: "E",
                damage: "9",
                heat: "9",
                crits: "5",
                rangePB: "-1",
                rangeS: "-1",
                rangeM: "1",
                rangeL: "3",
                rangeX: "9",
                useTC: "1"
            },
            flamer: {
                name: "Flamer",
                fullname: "Flamer",
                tech: "IS",
                type: "E",
                damage: "2",
                heat: "3",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useH: "2",
                specials: "ai"
            },
            erflamer: {
                name: "erFlamer",
                fullname: "ER Flamer",
                tech: "IS",
                type: "E",
                damage: "2",
                heat: "4",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                useH: "2",
                specials: "ai"
            },
            hflamer: {
                name: "HFlamer",
                fullname: "Heavy Flamer",
                tech: "IS",
                type: "E",
                damage: "4",
                heat: "5",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useH: "4",
                useAmmo: "Flamer",
                specials: "ai"
            },
            plasrifle: {
                name: "PlasRifle",
                fullname: "Plasma Rifle",
                tech: "IS",
                type: "E",
                damage: "10",
                heat: "10",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useH: "4",
                useTC: "1"
            },
            blazer: {
                name: "Blazer",
                fullname: "Binary (Blazer) Cannon",
                tech: "IS",
                type: "E",
                damage: "12",
                heat: "16",
                crits: "4",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1"
            },
            srm2: {
                name: "SRM-2",
                fullname: "SRM-2",
                tech: "IS",
                type: "M",
                damage: "1",
                damageAdj: "3",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv,av",
                useAmmo: "SRM",
                specials: "srm"
            },
            srm4: {
                name: "SRM-4",
                fullname: "SRM-4",
                tech: "IS",
                type: "M",
                damage: "8",
                heat: "3",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv,av",
                useAmmo: "SRM",
                specials: "srm"
            },
            srm6: {
                name: "SRM-6",
                fullname: "SRM-6",
                tech: "IS",
                type: "M",
                damage: "12",
                heat: "4",
                crits: "2",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv,av",
                useAmmo: "SRM",
                specials: "srm"
            },
            ssrm2: {
                name: "SSRM-2",
                fullname: "Streak SRM-2",
                tech: "IS",
                type: "M",
                damage: "1",
                damageAdj: "3",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SSRM",
                specials: "ssrm"
            },
            ssrm4: {
                name: "SSRM-4",
                fullname: "Streak SRM-4",
                tech: "IS",
                type: "M",
                damage: "8",
                heat: "3",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SSRM",
                specials: "ssrm"
            },
            ssrm6: {
                name: "SSRM-6",
                fullname: "Streak SRM-6",
                tech: "IS",
                type: "M",
                damage: "12",
                heat: "4",
                crits: "2",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SSRM",
                specials: "ssrm"
            },
            mrm10: {
                name: "MRM-10",
                fullname: "MRM-10",
                tech: "IS",
                type: "M",
                damage: "6",
                damageAdj: "4",
                heat: "4",
                crits: "2",
                damageM: "1",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useFCS: "apollo",
                useAmmo: "MRM",
                specials: "mrm"
            },
            mrm20: {
                name: "MRM-20",
                fullname: "MRM-20",
                tech: "IS",
                type: "M",
                damage: "12",
                damageAdj: "8",
                heat: "6",
                crits: "3",
                damageM: "2",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useFCS: "apollo",
                useAmmo: "MRM",
                specials: "mrm"
            },
            mrm30: {
                name: "MRM-30",
                fullname: "MRM-30",
                tech: "IS",
                type: "M",
                damage: "18",
                damageAdj: "12",
                heat: "10",
                crits: "5",
                damageM: "3",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useFCS: "apollo",
                specials: "mrm"
            },
            mrm40: {
                name: "MRM-40",
                fullname: "MRM-40",
                tech: "IS",
                type: "M",
                damage: "24",
                damageAdj: "16",
                heat: "12",
                crits: "7",
                damageM: "4",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useFCS: "apollo",
                specials: "mrm"
            },
            lrm5: {
                name: "LRM-5",
                fullname: "LRM-5",
                tech: "IS",
                type: "M",
                damage: "1",
                damageAdj: "4",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv,av",
                useAmmo: "LRM",
                specials: "lrm"
            },
            lrm10: {
                name: "LRM-10",
                fullname: "LRM-10",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "7",
                heat: "4",
                crits: "2",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv,av",
                useAmmo: "LRM",
                specials: "lrm"
            },
            lrm15: {
                name: "LRM-15",
                fullname: "LRM-15",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "12",
                heat: "5",
                crits: "3",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv,av",
                useAmmo: "LRM",
                specials: "lrm"
            },
            lrm20: {
                name: "LRM-20",
                fullname: "LRM-20",
                tech: "IS",
                type: "M",
                damage: "9",
                damageAdj: "11",
                heat: "6",
                crits: "5",
                damageM: "2",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv,av",
                useAmmo: "LRM",
                specials: "lrm"
            },
            nlrm5: {
                name: "nLRM-5",
                fullname: "Enhanced LRM-5",
                tech: "IS",
                type: "M",
                damage: "1",
                damageAdj: "4",
                heat: "2",
                crits: "2",
                damageM: "1",
                shiftM: "0",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRM",
                specials: "lrm"
            },
            nlrm10: {
                name: "nLRM-10",
                fullname: "Enhanced LRM-10",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "7",
                heat: "4",
                crits: "4",
                damageM: "1",
                shiftM: "0",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRM",
                specials: "lrm"
            },
            nlrm15: {
                name: "nLRM-15",
                fullname: "Enhanced LRM-15",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "12",
                heat: "5",
                crits: "6",
                damageM: "1",
                shiftM: "0",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRM",
                specials: "lrm"
            },
            nlrm20: {
                name: "nLRM-20",
                fullname: "Enhanced LRM-20",
                tech: "IS",
                type: "M",
                damage: "9",
                damageAdj: "11",
                heat: "6",
                crits: "9",
                damageM: "2",
                shiftM: "0",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRM",
                specials: "lrm"
            },
            elrm5: {
                name: "eLRM-5",
                fullname: "Extended LRM-5",
                tech: "IS",
                type: "M",
                damage: "5",
                heat: "3",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "0",
                rangeX: "2",
                varPBSdamage: "0",
                varMdamage: "0",
                varLXdamage: "1",
                useAmmo: "LRM",
                specials: "lrm, var"
            },
            elrm10: {
                name: "eLRM-10",
                fullname: "Extended LRM-10",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "7",
                heat: "6",
                crits: "4",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "0",
                rangeX: "2",
                varPBSdamage: "0",
                varMdamage: "0",
                varLXdamage: "2",
                useAmmo: "LRM",
                specials: "lrm, var"
            },
            elrm15: {
                name: "eLRM-15",
                fullname: "Extended LRM-15",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "12",
                heat: "8",
                crits: "6",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "0",
                rangeX: "2",
                varPBSdamage: "0",
                varMdamage: "0",
                varLXdamage: "3",
                useAmmo: "LRM",
                specials: "lrm, var"
            },
            elrm20: {
                name: "eLRM-20",
                fullname: "Extended LRM-20",
                tech: "IS",
                type: "M",
                damage: "9",
                damageAdj: "11",
                heat: "12",
                crits: "8",
                damageM: "2",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "0",
                rangeX: "2",
                varPBSdamage: "3",
                varMdamage: "3",
                varLXdamage: "5",
                useAmmo: "LRM",
                specials: "lrm, var"
            },
            tbolt5: {
                name: "TBolt-5",
                fullname: "Thunderbolt 5",
                tech: "IS",
                type: "M",
                damage: "5",
                heat: "3",
                crits: "1",
                rangePB: "4",
                rangeS: "2",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useAmmo: "TBolt",
                specials: ""
            },
            tbolt10: {
                name: "TBolt-10",
                fullname: "Thunderbolt 10",
                tech: "IS",
                type: "M",
                damage: "10",
                heat: "5",
                crits: "2",
                rangePB: "4",
                rangeS: "2",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useAmmo: "TBolt",
                specials: ""
            },
            tbolt15: {
                name: "TBolt-15",
                fullname: "Thunderbolt 15",
                tech: "IS",
                type: "M",
                damage: "15",
                heat: "7",
                crits: "3",
                rangePB: "4",
                rangeS: "2",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useAmmo: "TBolt",
                specials: ""
            },
            tbolt20: {
                name: "TBolt-20",
                fullname: "Thunderbolt 20",
                tech: "IS",
                type: "M",
                damage: "20",
                heat: "8",
                crits: "5",
                rangePB: "2",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useAmmo: "TBolt",
                specials: ""
            },
            mml3: {
                name: "MML-3",
                fullname: "MML-3",
                tech: "IS",
                type: "M",
                damage: "6",
                heat: "2",
                crits: "2",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "4",
                varPBSdamage: "3",
                varMdamage: "1",
                varLXdamage: "0",
                useFCS: "aiv",
                useAmmo: "MML",
                specials: "var"
            },
            mml5: {
                name: "MML-5",
                fullname: "MML-5",
                tech: "IS",
                type: "M",
                damage: "9",
                heat: "3",
                crits: "3",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "4",
                varPBSdamage: "3",
                varMdamage: "2",
                varLXdamage: "0",
                useFCS: "aiv",
                useAmmo: "MML",
                specials: "var"
            },
            mml7: {
                name: "MML-7",
                fullname: "MML-7",
                tech: "IS",
                type: "M",
                damage: "12",
                heat: "4",
                crits: "4",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "4",
                varPBSdamage: "5",
                varMdamage: "3",
                varLXdamage: "1",
                useFCS: "aiv",
                useAmmo: "MML",
                specials: "var"
            },
            mml9: {
                name: "MML-9",
                fullname: "MML-9",
                tech: "IS",
                type: "M",
                damage: "15",
                heat: "5",
                crits: "5",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "4",
                varPBSdamage: "6",
                varMdamage: "4",
                varLXdamage: "2",
                useFCS: "aiv",
                useAmmo: "MML",
                specials: "var"
            },
            rl10: {
                name: "RL10",
                fullname: "Rocket Launcher 10",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "6",
                heat: "3",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                specials: "rl, os"
            },
            rl15: {
                name: "RL15",
                fullname: "Rocket Launcher 15",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "12",
                heat: "4",
                crits: "2",
                damageM: "1",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                specials: "rl, os"
            },
            rl20: {
                name: "RL20",
                fullname: "Rocket Launcher 20",
                tech: "IS",
                type: "M",
                damage: "9",
                damageAdj: "11",
                heat: "5",
                crits: "3",
                damageM: "2",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "9",
                rangeX: "9",
                specials: "rl, os"
            },
            srt2: {
                name: "SRT-2",
                fullname: "SRT-2",
                tech: "IS",
                type: "M",
                damage: "1",
                damageAdj: "3",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv",
                useAmmo: "SRT",
                specials: "srt"
            },
            srt4: {
                name: "SRT-4",
                fullname: "SRT-4",
                tech: "IS",
                type: "M",
                damage: "8",
                heat: "3",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv",
                useAmmo: "SRT",
                specials: "srt"
            },
            srt6: {
                name: "SRT-6",
                fullname: "SRT-6",
                tech: "IS",
                type: "M",
                damage: "12",
                heat: "4",
                crits: "2",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv",
                useAmmo: "SRT",
                specials: "srt"
            },
            lrt5: {
                name: "LRT-5",
                fullname: "LRT-5",
                tech: "IS",
                type: "M",
                damage: "1",
                damageAdj: "4",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRT",
                specials: "lrt"
            },
            lrt10: {
                name: "LRT-10",
                fullname: "LRT-10",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "7",
                heat: "4",
                crits: "2",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRT",
                specials: "lrt"
            },
            lrt15: {
                name: "LRT-15",
                fullname: "LRT-15",
                tech: "IS",
                type: "M",
                damage: "3",
                damageAdj: "12",
                heat: "5",
                crits: "3",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRT",
                specials: "lrt"
            },
            lrt20: {
                name: "LRT-20",
                fullname: "LRT-20",
                tech: "IS",
                type: "M",
                damage: "9",
                damageAdj: "11",
                heat: "6",
                crits: "5",
                damageM: "2",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRT",
                specials: "lrt"
            },
            narc: {
                name: "Narc",
                fullname: "Narc Missile Beacon",
                tech: "IS",
                type: "M",
                damage: "0",
                heat: "0",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "Narc"
            },
            inarc: {
                name: "iNarc",
                fullname: "Improved Narc Missile Beacon",
                tech: "IS",
                type: "M",
                damage: "0",
                heat: "0",
                crits: "3",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useAmmo: "Narc"
            },
            clb2x: {
                name: "cLB 2-X",
                fullname: "Clan LB 2-X Autocannon",
                tech: "Clan",
                type: "B",
                damage: "2",
                heat: "1",
                crits: "3",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "2",
                useTC: "1",
                useAmmo: "LBX"
            },
            clb5x: {
                name: "cLB 5-X",
                fullname: "Clan LB 5-X Autocannon",
                tech: "Clan",
                type: "B",
                damage: "5",
                heat: "1",
                crits: "4",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useC: "1",
                useTC: "1",
                useAmmo: "LBX"
            },
            clb10x: {
                name: "cLB 10-X",
                fullname: "Clan LB 10-X Autocannon",
                tech: "Clan",
                type: "B",
                damage: "10",
                heat: "2",
                crits: "5",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useC: "1",
                useTC: "1",
                useAmmo: "LBX"
            },
            clb20x: {
                name: "cLB 20-X",
                fullname: "Clan LB 20-X Autocannon",
                tech: "Clan",
                type: "B",
                damage: "20",
                heat: "6",
                crits: "9",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useC: "1",
                useTC: "1",
                useAmmo: "LBX"
            },
            cuac2: {
                name: "cUAC/2",
                fullname: "Clan Ultra Autocannon/2",
                tech: "Clan",
                type: "B",
                damage: "2",
                heat: "1",
                crits: "2",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "2",
                useR: "2",
                useTC: "1",
                useAmmo: "UAC"
            },
            cuac5: {
                name: "cUAC/5",
                fullname: "Clan Ultra Autocannon/5",
                tech: "Clan",
                type: "B",
                damage: "5",
                heat: "1",
                crits: "3",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useR: "5",
                useTC: "1",
                useAmmo: "UAC"
            },
            cuac10: {
                name: "cUAC/10",
                fullname: "Clan Ultra Autocannon/10",
                tech: "Clan",
                type: "B",
                damage: "10",
                heat: "3",
                crits: "4",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useR: "10",
                useTC: "1",
                useAmmo: "UAC"
            },
            cuac20: {
                name: "cUAC/20",
                fullname: "Clan Ultra Autocannon/20",
                tech: "Clan",
                type: "B",
                damage: "20",
                heat: "7",
                crits: "8",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useR: "20",
                useTC: "1",
                useAmmo: "UAC"
            },
            crac2: {
                name: "cRAC/2",
                fullname: "Clan Rotary Autocannon/2",
                tech: "Clan",
                type: "B",
                damage: "3",
                heat: "3",
                crits: "4",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "2",
                useR: "6",
                useTC: "1",
                useAmmo: "RAC"
            },
            crac5: {
                name: "cRAC/5",
                fullname: "Clan Rotary Autocannon/5",
                tech: "Clan",
                type: "B",
                damage: "8",
                heat: "3",
                crits: "8",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useR: "12",
                useTC: "1",
                useAmmo: "RAC"
            },
            capgauss: {
                name: "cAPGauss",
                fullname: "Clan AP Gauss Rifle",
                tech: "Clan",
                type: "B",
                damage: "3",
                heat: "1",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1",
                useAmmo: "Gauss",
                specials: "ai"
            },
            cgauss: {
                name: "cGauss",
                fullname: "Clan Gauss Rifle",
                tech: "Clan",
                type: "B",
                damage: "15",
                heat: "1",
                crits: "6",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useTC: "1",
                useAmmo: "Gauss"
            },
            chag20: {
                name: "cHAG 20",
                fullname: "Clan Hyper-Assault Gauss Rifle 20",
                tech: "Clan",
                type: "B",
                damage: "16",
                heat: "4",
                crits: "6",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                varPBSdamage: "16",
                varMdamage: "13",
                varLXdamage: "11",
                useC: "1",
                useTC: "1",
                useAmmo: "HAG",
                specials: "var,hag20"
            },
            chag30: {
                name: "cHAG 30",
                fullname: "Clan Hyper-Assault Gauss Rifle 30",
                tech: "Clan",
                type: "B",
                damage: "23",
                heat: "6",
                crits: "8",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                varPBSdamage: "23",
                varMdamage: "19",
                varLXdamage: "16",
                useC: "1",
                useTC: "1",
                useAmmo: "HAG",
                specials: "var,hag30"
            },
            chag40: {
                name: "cHAG 40",
                fullname: "Clan Hyper-Assault Gauss Rifle 40",
                tech: "Clan",
                type: "B",
                damage: "31",
                heat: "8",
                crits: "10",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                varPBSdamage: "31",
                varMdamage: "26",
                varLXdamage: "17",
                useC: "1",
                useTC: "1",
                useAmmo: "HAG",
                specials: "var,hag40"
            },
            clmg: {
                name: "cLMG",
                fullname: "Clan Light Machine Gun",
                tech: "Clan",
                type: "B",
                damage: "1",
                heat: "0",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "MG",
                specials: "ai"
            },
            cmg: {
                name: "cMG",
                fullname: "Clan Machine Gun",
                tech: "Clan",
                type: "B",
                damage: "2",
                heat: "0",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "MG",
                specials: "ai"
            },
            chmg: {
                name: "cHMG",
                fullname: "Clan Heavy Machine Gun",
                tech: "Clan",
                type: "B",
                damage: "3",
                heat: "0",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "MG",
                specials: "ai"
            },
            cpmac2: {
                name: "cPMAC/2",
                fullname: "Clan ProtoMech Autocannon/2",
                tech: "IS",
                type: "B",
                damage: "2",
                heat: "1",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useTC: "1",
                useAmmo: "AC"
            },
            cpmac4: {
                name: "cPMAC/4",
                fullname: "Clan ProtoMech Autocannon/4",
                tech: "IS",
                type: "B",
                damage: "4",
                heat: "1",
                crits: "3",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1",
                useAmmo: "AC"
            },
            cpmac8: {
                name: "cPMAC/8",
                fullname: "Clan ProtoMech Autocannon/8",
                tech: "IS",
                type: "B",
                damage: "8",
                heat: "2",
                crits: "4",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1",
                useAmmo: "AC"
            },
            cnailrivet: {
                name: "cNailRivet",
                fullname: "Clan Nail/Rivet Gun",
                tech: "Clan",
                type: "B",
                damage: "0",
                heat: "0",
                crits: "1",
                rangePB: "0",
                rangeS: "9",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: "ai"
            },
            cermiclas: {
                name: "cermicLas",
                fullname: "Clan ER Micro Laser",
                tech: "Clan",
                type: "E",
                damage: "2",
                heat: "1",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            cerslas: {
                name: "cerSLas",
                fullname: "Clan ER Small Laser",
                tech: "Clan",
                type: "E",
                damage: "5",
                heat: "2",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            cermlas: {
                name: "cerMLas",
                fullname: "Clan ER Medium Laser",
                tech: "Clan",
                type: "E",
                damage: "7",
                heat: "5",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1"
            },
            cerllas: {
                name: "cerLLas",
                fullname: "Clan ER Large Laser",
                tech: "Clan",
                type: "E",
                damage: "10",
                heat: "12",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "2",
                useTC: "1"
            },
            cerppc: {
                name: "cerPPC",
                fullname: "Clan ER PPC",
                tech: "Clan",
                type: "E",
                damage: "15",
                heat: "15",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useTC: "1"
            },
            cmicplas: {
                name: "cmicPLas",
                fullname: "Clan Micro Pulse Laser",
                tech: "Clan",
                type: "E",
                damage: "3",
                heat: "1",
                crits: "1",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useTC: "1",
                specials: "ai"
            },
            csplas: {
                name: "cSPLas",
                fullname: "Clan Small Pulse Laser",
                tech: "Clan",
                type: "E",
                damage: "3",
                heat: "2",
                crits: "1",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1",
                specials: "ai"
            },
            cmplas: {
                name: "cMPLas",
                fullname: "Clan Medium Pulse Laser",
                tech: "Clan",
                type: "E",
                damage: "7",
                heat: "4",
                crits: "1",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "0",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            clplas: {
                name: "cLPLas",
                fullname: "Clan Large Pulse Laser",
                tech: "Clan",
                type: "E",
                damage: "10",
                heat: "10",
                crits: "2",
                rangePB: "-2",
                rangeS: "-2",
                rangeM: "-2",
                rangeL: "0",
                rangeX: "2",
                useTC: "1"
            },
            cersplas: {
                name: "cerSPLas",
                fullname: "Clan ER Small Pulse Laser",
                tech: "Clan",
                type: "E",
                damage: "5",
                heat: "3",
                crits: "1",
                rangePB: "-1",
                rangeS: "-1",
                rangeM: "3",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            cermplas: {
                name: "cerMPLas",
                fullname: "Clan ER Medium Pulse Laser",
                tech: "Clan",
                type: "E",
                damage: "7",
                heat: "6",
                crits: "2",
                rangePB: "-1",
                rangeS: "-1",
                rangeM: "1",
                rangeL: "3",
                rangeX: "9",
                useTC: "1"
            },
            cerlplas: {
                name: "cerLPLas",
                fullname: "Clan ER Large Pulse Laser",
                tech: "Clan",
                type: "E",
                damage: "10",
                heat: "13",
                crits: "3",
                rangePB: "-1",
                rangeS: "-1",
                rangeM: "-1",
                rangeL: "1",
                rangeX: "3",
                useTC: "1"
            },
            chslas: {
                name: "cHSLas",
                fullname: "Clan Heavy Small Laser",
                tech: "Clan",
                type: "E",
                damage: "6",
                heat: "3",
                crits: "1",
                rangePB: "1",
                rangeS: "1",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            chmlas: {
                name: "cHMLas",
                fullname: "Clan Heavy Medium Laser",
                tech: "Clan",
                type: "E",
                damage: "10",
                heat: "7",
                crits: "2",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            chllas: {
                name: "cHLLas",
                fullname: "Clan Heavy Large Laser",
                tech: "Clan",
                type: "E",
                damage: "16",
                heat: "18",
                crits: "3",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useTC: "1"
            },
            cihslas: {
                name: "ciHSLas",
                fullname: "Clan Improved Heavy Small Laser",
                tech: "Clan",
                type: "E",
                damage: "6",
                heat: "3",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            cihmlas: {
                name: "ciHMLas",
                fullname: "Clan Improved Heavy Medium Laser",
                tech: "Clan",
                type: "E",
                damage: "10",
                heat: "7",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            cihllas: {
                name: "ciHLLas",
                fullname: "Clan Improved Heavy Large Laser",
                tech: "Clan",
                type: "E",
                damage: "16",
                heat: "18",
                crits: "3",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1"
            },
            cchemslas: {
                name: "cChemSLas",
                fullname: "Chemical Small Laser",
                tech: "Clan",
                type: "E",
                damage: "3",
                heat: "1",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            cchemmlas: {
                name: "cChemMLas",
                fullname: "Chemical Medium Laser",
                tech: "Clan",
                type: "E",
                damage: "5",
                heat: "2",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useTC: "1"
            },
            cchemllas: {
                name: "cChemLLas",
                fullname: "Chemical Large Laser",
                tech: "Clan",
                type: "E",
                damage: "8",
                heat: "6",
                crits: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useTC: "1"
            },
            cflamer: {
                name: "cFlamer",
                fullname: "Clan Flamer",
                tech: "Clan",
                type: "E",
                damage: "2",
                heat: "3",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useH: "2",
                specials: "ai"
            },
            cerflamer: {
                name: "cerFlamer",
                fullname: "Clan ER Flamer",
                tech: "Clan",
                type: "E",
                damage: "2",
                heat: "4",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                useH: "2",
                specials: "ai"
            },
            chflamer: {
                name: "cHFlamer",
                fullname: "Clan Heavy Flamer",
                tech: "Clan",
                type: "E",
                damage: "4",
                heat: "5",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useH: "4",
                useAmmo: "Flamer",
                specials: "ai"
            },
            cplascannon: {
                name: "cPlasCannon",
                fullname: "Clan Plasma Cannon",
                tech: "Clan",
                type: "E",
                damage: "0",
                heat: "7",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useH: "8",
                useTC: "1"
            },
            csrm2: {
                name: "cSRM-2",
                fullname: "Clan SRM-2",
                tech: "Clan",
                type: "M",
                damage: "1",
                damageAdj: "3",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv,av",
                useAmmo: "SRM",
                specials: "srm"
            },
            csrm4: {
                name: "cSRM-4",
                fullname: "Clan SRM-4",
                tech: "Clan",
                type: "M",
                damage: "8",
                heat: "3",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv,av",
                useAmmo: "SRM",
                specials: "srm"
            },
            csrm6: {
                name: "cSRM-6",
                fullname: "Clan SRM-6",
                tech: "Clan",
                type: "M",
                damage: "12",
                heat: "4",
                crits: "1",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv,av",
                useAmmo: "SRM",
                specials: "srm"
            },
            cssrm2: {
                name: "cSSRM-2",
                fullname: "Clan Streak SRM-2",
                tech: "Clan",
                type: "M",
                damage: "1",
                damageAdj: "3",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SSRM",
                specials: "ssrm"
            },
            cssrm4: {
                name: "cSSRM-4",
                fullname: "Clan Streak SRM-4",
                tech: "Clan",
                type: "M",
                damage: "8",
                heat: "3",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SSRM",
                specials: "ssrm"
            },
            cssrm6: {
                name: "cSSRM-6",
                fullname: "Clan Streak SRM-6",
                tech: "Clan",
                type: "M",
                damage: "12",
                heat: "4",
                crits: "2",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SSRM",
                specials: "ssrm"
            },
            clrm5: {
                name: "cLRM-5",
                fullname: "Clan LRM-5",
                tech: "Clan",
                type: "M",
                damage: "1",
                damageAdj: "4",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv,av",
                useAmmo: "LRM",
                specials: "lrm"
            },
            clrm10: {
                name: "cLRM-10",
                fullname: "Clan LRM-10",
                tech: "Clan",
                type: "M",
                damage: "3",
                damageAdj: "7",
                heat: "4",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv,av",
                useAmmo: "LRM",
                specials: "lrm"
            },
            clrm15: {
                name: "cLRM-15",
                fullname: "Clan LRM-15",
                tech: "Clan",
                type: "M",
                damage: "3",
                damageAdj: "12",
                heat: "5",
                crits: "2",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv,av",
                useAmmo: "LRM"
            },
            clrm20: {
                name: "cLRM-20",
                fullname: "Clan LRM-20",
                tech: "Clan",
                type: "M",
                damage: "9",
                damageAdj: "11",
                heat: "6",
                crits: "4",
                damageM: "2",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv,av",
                useAmmo: "LRM",
                specials: "lrm"
            },
            cslrm5: {
                name: "cSLRM-5",
                fullname: "Clan Streak LRM-5",
                tech: "Clan",
                type: "M",
                damage: "1",
                damageAdj: "4",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "SLRM",
                specials: "slrm"
            },
            cslrm10: {
                name: "cSLRM-10",
                fullname: "Clan Streak LRM-10",
                tech: "Clan",
                type: "M",
                damage: "3",
                damageAdj: "7",
                heat: "4",
                crits: "2",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "SLRM",
                specials: "slrm"
            },
            cslrm15: {
                name: "cSLRM-15",
                fullname: "Clan Streak LRM-15",
                tech: "Clan",
                type: "M",
                damage: "3",
                damageAdj: "12",
                heat: "5",
                crits: "3",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "SLRM",
                specials: "slrm"
            },
            cslrm20: {
                name: "cSLRM-20",
                fullname: "Clan Streak LRM-20",
                tech: "Clan",
                type: "M",
                damage: "9",
                damageAdj: "11",
                heat: "6",
                crits: "5",
                damageM: "2",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "SLRM",
                specials: "slrm"
            },
            catm3: {
                name: "cATM-3",
                fullname: "Clan ATM-3",
                tech: "Clan",
                type: "M",
                damage: "7",
                heat: "2",
                crits: "2",
                damageM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "2",
                varPBSdamage: "3",
                varMdamage: "1",
                varLXdamage: "0",
                useAmmo: "ATM",
                specials: "atm, var"
            },
            catm6: {
                name: "cATM-6",
                fullname: "Clan ATM-6",
                tech: "Clan",
                type: "M",
                damage: "15",
                heat: "4",
                crits: "3",
                damageM: "3",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "2",
                varPBSdamage: "5",
                varMdamage: "1",
                varLXdamage: "0",
                useAmmo: "ATM",
                specials: "atm, var"
            },
            catm9: {
                name: "cATM-9",
                fullname: "Clan ATM-9",
                tech: "Clan",
                type: "M",
                damage: "24",
                heat: "6",
                crits: "4",
                damageM: "6",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "2",
                varPBSdamage: "7",
                varMdamage: "3",
                varLXdamage: "0",
                useAmmo: "ATM",
                specials: "atm, var"
            },
            catm12: {
                name: "cATM-12",
                fullname: "Clan ATM-12",
                tech: "Clan",
                type: "M",
                damage: "33",
                heat: "8",
                crits: "5",
                damageM: "6",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "2",
                varPBSdamage: "14",
                varMdamage: "9",
                varLXdamage: "3",
                useAmmo: "ATM",
                specials: "atm, var"
            },
            ciatm3: {
                name: "ciATM-3",
                fullname: "Clan iATM-3",
                tech: "Clan",
                type: "M",
                damage: "7",
                heat: "2",
                crits: "2",
                damageM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "2",
                varPBSdamage: "3",
                varMdamage: "1",
                varLXdamage: "0",
                useAmmo: "ATM",
                specials: "iatm, var"
            },
            ciatm6: {
                name: "ciATM-6",
                fullname: "Clan iATM-6",
                tech: "Clan",
                type: "M",
                damage: "15",
                heat: "4",
                crits: "3",
                damageM: "3",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "2",
                varPBSdamage: "5",
                varMdamage: "1",
                varLXdamage: "0",
                useAmmo: "ATM",
                specials: "iatm, var"
            },
            ciatm9: {
                name: "ciATM-9",
                fullname: "Clan iATM-9",
                tech: "Clan",
                type: "M",
                damage: "24",
                heat: "6",
                crits: "4",
                damageM: "6",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "2",
                varPBSdamage: "7",
                varMdamage: "3",
                varLXdamage: "0",
                useAmmo: "ATM",
                specials: "iatm, var"
            },
            ciatm12: {
                name: "ciATM-12",
                fullname: "Clan iATM-12",
                tech: "Clan",
                type: "M",
                damage: "33",
                heat: "8",
                crits: "5",
                damageM: "6",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "2",
                rangeX: "2",
                varPBSdamage: "14",
                varMdamage: "9",
                varLXdamage: "3",
                useAmmo: "ATM",
                specials: "iatm, var"
            },
            csrt2: {
                name: "cSRT-2",
                fullname: "Clan SRT-2",
                tech: "Clan",
                type: "M",
                damage: "1",
                damageAdj: "3",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv",
                useAmmo: "SRT",
                specials: "srt"
            },
            csrt4: {
                name: "cSRT-4",
                fullname: "Clan SRT-4",
                tech: "Clan",
                type: "M",
                damage: "8",
                heat: "3",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv",
                useAmmo: "SRT",
                specials: "srt"
            },
            csrt6: {
                name: "cSRT-6",
                fullname: "Clan SRT-6",
                tech: "Clan",
                type: "M",
                damage: "12",
                heat: "4",
                crits: "1",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useFCS: "aiv",
                useAmmo: "SRT",
                specials: "srt"
            },
            clrt5: {
                name: "cLRT-5",
                fullname: "Clan LRT-5",
                tech: "Clan",
                type: "M",
                damage: "1",
                damageAdj: "4",
                heat: "2",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRT",
                specials: "lrt"
            },
            clrt10: {
                name: "cLRT-10",
                fullname: "Clan LRT-10",
                tech: "Clan",
                type: "M",
                damage: "3",
                damageAdj: "7",
                heat: "4",
                crits: "1",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRT",
                specials: "lrt"
            },
            clrt15: {
                name: "cLRT-15",
                fullname: "Clan LRT-15",
                tech: "Clan",
                type: "M",
                damage: "3",
                damageAdj: "12",
                heat: "5",
                crits: "2",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRT",
                specials: "lrt"
            },
            clrt20: {
                name: "cLRT-20",
                fullname: "Clan LRT-20",
                tech: "Clan",
                type: "M",
                damage: "9",
                damageAdj: "11",
                heat: "6",
                crits: "4",
                damageM: "2",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useFCS: "aiv",
                useAmmo: "LRT",
                specials: "lrt"
            },
            cnarc: {
                name: "cNarc",
                fullname: "Clan Narc Missile Beacon",
                tech: "Clan",
                type: "M",
                damage: "0",
                heat: "0",
                crits: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "Narc"
            },
            arrowiv: {
                name: "Arrow IV",
                fullname: "Arrow IV Artillery",
                tech: "IS",
                type: "M",
                damage: "20",
                heat: "10",
                crits: "15",
                damageM: "4",
                shiftM: "0",
                rangePB: "9",
                rangeS: "4",
                rangeM: "4",
                rangeL: "4",
                rangeX: "4",
                useAmmo: "ArrowIV",
                specials: "art,extraM"
            },
            carrowiv: {
                name: "cArrow IV",
                fullname: "Clan Arrow IV Artillery",
                tech: "Clan",
                type: "M",
                damage: "20",
                heat: "10",
                crits: "12",
                damageM: "4",
                shiftM: "0",
                rangePB: "9",
                rangeS: "4",
                rangeM: "4",
                rangeL: "4",
                rangeX: "4",
                useAmmo: "ArrowIV",
                specials: "art,extraM"
            },
            longtom: {
                name: "Long Tom",
                fullname: "Long Tom Artillery",
                tech: "IS",
                type: "M",
                damage: "30",
                heat: "20",
                crits: "30",
                damageM: "6",
                shiftM: "3",
                rangePB: "9",
                rangeS: "4",
                rangeM: "4",
                rangeL: "4",
                rangeX: "4",
                useAmmo: "Artillery",
                specials: "art"
            },
            sniper: {
                name: "Sniper",
                fullname: "Sniper Artillery",
                tech: "IS",
                type: "M",
                damage: "20",
                heat: "10",
                crits: "20",
                damageM: "4",
                shiftM: "2",
                rangePB: "9",
                rangeS: "4",
                rangeM: "4",
                rangeL: "4",
                rangeX: "4",
                useAmmo: "Artillery",
                specials: "art,extraM"
            },
            thumper: {
                name: "Thumper",
                fullname: "Thumper Artillery",
                tech: "IS",
                type: "M",
                damage: "15",
                heat: "6",
                crits: "15",
                damageM: "3",
                shiftM: "1",
                rangePB: "9",
                rangeS: "4",
                rangeM: "4",
                rangeL: "4",
                rangeX: "4",
                useAmmo: "Artillery",
                specials: "art,extraM"
            },
            longtomcannon: {
                name: "Long Tom Cannon",
                fullname: "Long Tom Artillery Cannon",
                tech: "IS",
                type: "M",
                damage: "20",
                heat: "20",
                crits: "15",
                damageM: "4",
                shiftM: "1",
                rangePB: "2",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "Artillery",
                specials: "art,extraM"
            },
            snipercannon: {
                name: "Sniper Cannon",
                fullname: "Sniper Artillery Cannon",
                tech: "IS",
                type: "M",
                damage: "10",
                heat: "10",
                crits: "10",
                damageM: "2",
                shiftM: "0",
                rangePB: "2",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "Artillery",
                specials: "art,extraM"
            },
            thumpercannon: {
                name: "Thumper Cannon",
                fullname: "Thumper Artillery Cannon",
                tech: "IS",
                type: "M",
                damage: "5",
                heat: "6",
                crits: "7",
                damageM: "1",
                rangePB: "2",
                rangeS: "0",
                rangeM: "2",
                rangeL: "4",
                rangeX: "9",
                useAmmo: "Artillery",
                specials: "art,extraM"
            },
            hatchet: {
                name: "Hatchet",
                fullname: "Hatchet",
                tech: "Mixed",
                type: "P",
                damage: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 5),
                heat: "0",
                crits: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 15),
                rangePB: "-1",
                rangeS: "9",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: ""
            },
            sword: {
                name: "Sword",
                fullname: "Sword",
                tech: "Mixed",
                type: "P",
                damage: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 10),
                heat: "0",
                crits: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 15),
                rangePB: "-2",
                rangeS: "9",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: ""
            },
            mace: {
                name: "Mace",
                fullname: "Mace",
                tech: "Mixed",
                type: "P",
                damage: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 4),
                heat: "0",
                crits: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 10),
                rangePB: "1",
                rangeS: "9",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: ""
            },
            claws: {
                name: "Claws",
                fullname: "Claws",
                tech: "Mixed",
                type: "P",
                damage: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 7),
                heat: "0",
                crits: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 15),
                rangePB: "1",
                rangeS: "9",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: ""
            },
            lance: {
                name: "Lance",
                fullname: "Lance",
                tech: "Mixed",
                type: "P",
                damage: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 5),
                heat: "0",
                crits: e => Math.ceil(((null === e || void 0 === e ? void 0 : e.tonnage) || 0) / 20),
                rangePB: "1",
                rangeS: "9",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: ""
            },
            firedrake: {
                name: "FNeedler",
                fullname: '"Firedrake" Support Needler',
                tech: "IS",
                type: "B",
                damage: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: "ai"
            },
            david: {
                name: "DLGauss",
                fullname: '"David" Light Gauss Rifle',
                tech: "IS",
                type: "B",
                damage: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                baOnly: !0
            },
            kdavid: {
                name: "KDLGauss",
                fullname: '"King David" Light Gauss Rifle',
                tech: "IS",
                type: "B",
                damage: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                baOnly: !0
            },
            gmauler: {
                name: "GM Gauss Cannon",
                fullname: "Grand Mauler Gauss Cannon",
                tech: "IS",
                type: "B",
                damage: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                baOnly: !0
            },
            tsunami: {
                name: "T Gauss",
                fullname: "Tsunami Gauss Rifle",
                tech: "IS",
                type: "B",
                damage: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                baOnly: !0
            },
            mgrenade: {
                name: "mGrenade Launcher",
                fullname: "Micro Grenade Launcher",
                tech: "IS",
                type: "B",
                damage: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: "ai",
                baOnly: !0
            },
            hgrenade: {
                name: "HGrenade Launcher",
                fullname: "Heavy Grenade Launcher",
                tech: "Mixed",
                type: "B",
                damage: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: "ai",
                baOnly: !0
            },
            lmortar: {
                name: "LMortar",
                fullname: "Light Mortar",
                tech: "Mixed",
                type: "B",
                damage: "3",
                rangePB: "2",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: "ai",
                baOnly: !0
            },
            hmortar: {
                name: "HMortar",
                fullname: "Heavy Mortar",
                tech: "Mixed",
                type: "B",
                damage: "3",
                rangePB: "2",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                specials: "ai",
                baOnly: !0
            },
            lrecoil: {
                name: "LRecoilless",
                fullname: "Light Recoilless Rifle",
                tech: "Mixed",
                type: "B",
                damage: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                specials: "ai",
                baOnly: !0
            },
            mrecoil: {
                name: "MRecoilless",
                fullname: "Medium Recoilless Rifle",
                tech: "Mixed",
                type: "B",
                damage: "3",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                specials: "ai",
                baOnly: !0
            },
            hrecoil: {
                name: "HRecoilless",
                fullname: "Heavy Recoilless Rifle",
                tech: "Mixed",
                type: "B",
                damage: "3",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                specials: "ai",
                baOnly: !0
            },
            mpplasrifle: {
                name: "mpPlasmaRifle",
                fullname: "Man-Portable Plasma Rifle",
                tech: "IS",
                type: "E",
                damage: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                useH: "2"
            },
            sppc: {
                name: "SPPC",
                fullname: "Support PPC",
                tech: "IS",
                type: "E",
                damage: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                baOnly: !0
            },
            compactnarc: {
                name: "Compact Narc",
                fullname: "Compact Narc",
                tech: "Mixed",
                type: "M",
                damage: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                baOnly: !0
            },
            srm1: {
                name: "SRM-1",
                fullname: "SRM-1",
                tech: "IS",
                type: "M",
                damage: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM",
                baOnly: !0
            },
            srm3: {
                name: "SRM-3",
                fullname: "SRM-3",
                tech: "IS",
                type: "M",
                damage: "6",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM",
                baOnly: !0
            },
            srm5: {
                name: "SRM-5",
                fullname: "SRM-5",
                tech: "IS",
                type: "M",
                damage: "10",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM",
                baOnly: !0
            },
            mrm1: {
                name: "MRM-1",
                fullname: "MRM-1",
                tech: "IS",
                type: "M",
                damage: "1",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useAmmo: "MRM",
                baOnly: !0
            },
            mrm2: {
                name: "MRM-2",
                fullname: "MRM-2",
                tech: "IS",
                type: "M",
                damage: "2",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useAmmo: "MRM",
                baOnly: !0
            },
            mrm3: {
                name: "MRM-3",
                fullname: "MRM-3",
                tech: "IS",
                type: "M",
                damage: "3",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useAmmo: "MRM",
                baOnly: !0
            },
            mrm4: {
                name: "MRM-4",
                fullname: "MRM-4",
                tech: "IS",
                type: "M",
                damage: "4",
                damageM: "1",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useAmmo: "MRM",
                baOnly: !0
            },
            mrm5: {
                name: "MRM-5",
                fullname: "MRM-5",
                tech: "IS",
                type: "M",
                damage: "5",
                damageM: "1",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "5",
                rangeX: "9",
                useAmmo: "MRM",
                baOnly: !0
            },
            lrm1: {
                name: "LRM-1",
                fullname: "LRM-1",
                tech: "IS",
                type: "M",
                damage: "1",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "LRM",
                baOnly: !0
            },
            lrm2: {
                name: "LRM-2",
                fullname: "LRM-2",
                tech: "IS",
                type: "M",
                damage: "2",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "LRM",
                baOnly: !0
            },
            lrm3: {
                name: "LRM-3",
                fullname: "LRM-3",
                tech: "IS",
                type: "M",
                damage: "3",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "LRM",
                baOnly: !0
            },
            lrm4: {
                name: "LRM-4",
                fullname: "LRM-4",
                tech: "IS",
                type: "M",
                damage: "4",
                damageM: "1",
                shiftM: "0",
                rangePB: "4",
                rangeS: "2",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "LRM",
                baOnly: !0
            },
            rl1: {
                name: "RL1",
                fullname: "Rocket Launcher 1",
                tech: "IS",
                type: "M",
                damage: "1",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "9",
                rangeX: "9",
                specials: "os",
                baOnly: !0
            },
            rl2: {
                name: "RL2",
                fullname: "Rocket Launcher 2",
                tech: "IS",
                type: "M",
                damage: "2",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "9",
                rangeX: "9",
                specials: "os",
                baOnly: !0
            },
            rl3: {
                name: "RL3",
                fullname: "Rocket Launcher 3",
                tech: "IS",
                type: "M",
                damage: "3",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "9",
                rangeX: "9",
                specials: "os",
                baOnly: !0
            },
            rl4: {
                name: "RL4",
                fullname: "Rocket Launcher 4",
                tech: "IS",
                type: "M",
                damage: "4",
                damageM: "1",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "9",
                rangeX: "9",
                specials: "os",
                baOnly: !0
            },
            rl5: {
                name: "RL5",
                fullname: "Rocket Launcher 5",
                tech: "IS",
                type: "M",
                damage: "5",
                damageM: "1",
                shiftM: "0",
                rangePB: "1",
                rangeS: "1",
                rangeM: "3",
                rangeL: "9",
                rangeX: "9",
                specials: "os",
                baOnly: !0
            },
            popmine: {
                name: "Mine Launcher",
                fullname: "Pop-up Mine Launcher",
                tech: "IS",
                type: "M",
                damage: "4",
                rangePB: "0",
                rangeS: "9",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                baOnly: !0
            },
            taser: {
                name: "Taser",
                fullname: "Battle Armor Taser",
                tech: "IS",
                type: "E",
                damage: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                baOnly: !0
            },
            bearhunt: {
                name: "SH AC",
                fullname: '"Bearhunter" Superheavy AC',
                tech: "Clan",
                type: "B",
                damage: "3",
                rangePB: "0",
                rangeS: "2",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                specials: "ai"
            },
            clbx: {
                name: "LB-X",
                fullname: "BA LB-X Autocannon",
                tech: "Clan",
                type: "B",
                damage: "4",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9",
                useC: "1",
                useAmmo: "LBX"
            },
            csppc: {
                name: "cSPPC",
                fullname: "Clan Support PPC",
                tech: "Clan",
                type: "E",
                damage: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "4",
                rangeL: "9",
                rangeX: "9"
            },
            csrm1: {
                name: "cSRM-1",
                fullname: "Clan SRM-1",
                tech: "Clan",
                type: "M",
                damage: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM"
            },
            csrm3: {
                name: "cSRM-3",
                fullname: "Clan SRM-3",
                tech: "Clan",
                type: "M",
                damage: "6",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM"
            },
            csrm5: {
                name: "cSRM-5",
                fullname: "Clan SRM-5",
                tech: "Clan",
                type: "M",
                damage: "10",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM"
            },
            casrm1: {
                name: "aSRM-1",
                fullname: "Clan Advanced SRM-1",
                tech: "Clan",
                type: "M",
                damage: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM"
            },
            casrm2: {
                name: "aSRM-2",
                fullname: "Clan Advanced SRM-2",
                tech: "Clan",
                type: "M",
                damage: "4",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM"
            },
            casrm3: {
                name: "aSRM-3",
                fullname: "Clan Advanced SRM-3",
                tech: "Clan",
                type: "M",
                damage: "6",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM"
            },
            casrm4: {
                name: "aSRM-4",
                fullname: "Clan Advanced SRM-4",
                tech: "Clan",
                type: "M",
                damage: "8",
                damageM: "1",
                shiftM: "0",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM"
            },
            casrm5: {
                name: "aSRM-5",
                fullname: "Clan Advanced SRM-5",
                tech: "Clan",
                type: "M",
                damage: "10",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM"
            },
            casrm6: {
                name: "aSRM-6",
                fullname: "Clan Advanced SRM-6",
                tech: "Clan",
                type: "M",
                damage: "12",
                damageM: "2",
                shiftM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "2",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "SRM"
            },
            clrm1: {
                name: "cLRM-1",
                fullname: "Clan LRM-1",
                tech: "Clan",
                type: "M",
                damage: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "LRM"
            },
            clrm2: {
                name: "cLRM-2",
                fullname: "Clan LRM-2",
                tech: "Clan",
                type: "M",
                damage: "2",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "LRM"
            },
            clrm3: {
                name: "cLRM-3",
                fullname: "Clan LRM-3",
                tech: "Clan",
                type: "M",
                damage: "3",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "LRM"
            },
            clrm4: {
                name: "cLRM-4",
                fullname: "Clan LRM-4",
                tech: "Clan",
                type: "M",
                damage: "4",
                damageM: "1",
                rangePB: "0",
                rangeS: "0",
                rangeM: "0",
                rangeL: "2",
                rangeX: "4",
                useAmmo: "LRM"
            },
            cbombrack: {
                name: "Bomb Rack",
                fullname: "Clan Bomb Rack",
                tech: "Clan",
                type: "M",
                damage: "2",
                rangePB: "0",
                rangeS: "9",
                rangeM: "9",
                rangeL: "9",
                rangeX: "9",
                useAmmo: "Bomb"
            }
        };
        class p {
            constructor(e, a) {
                this.unit = e,
                this.tic = (null === a || void 0 === a ? void 0 : a.tic) || 1,
                this._id = (null === a || void 0 === a ? void 0 : a.id) || "",
                this.location = (null === a || void 0 === a ? void 0 : a.location) || "",
                this._useOS = (null === a || void 0 === a ? void 0 : a.useOS) || !1,
                this._ammo = (null === a || void 0 === a ? void 0 : a.ammo) || p.AmmoTypeEnum.Std
            }
            get id() {
                return this._id
            }
            set id(e) {
                e !== this._id && (this._id = e,
                this._useOS = !1,
                this._ammo = p.AmmoTypeEnum.Std)
            }
            get name() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.name) || ""
            }
            get fullname() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.fullname) || ""
            }
            get tech() {
                var e;
                return A.TechEnum[null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.tech] || ""
            }
            get type() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.type) || ""
            }
            get damageAdj() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.damageAdj) || ""
            }
            get damage() {
                var e, a, t = (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.damage) || 0;
                ("function" === typeof t && (t = t(this.unit)),
                !0 === this.name.includes("PPC")) && ((null === (a = this.unit) || void 0 === a ? void 0 : a.hasPPCCapacitor(this.location)) > 0 && (t = Number(t),
                t += 5));
                return t
            }
            get heat() {
                var e, a, t = 0;
                return t = (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.heat) || 0,
                t = Number(t),
                !0 === this.name.includes("PPC") && (null === (a = this.unit) || void 0 === a ? void 0 : a.hasPPCCapacitor(this.location)) > 0 && (t += 5),
                t
            }
            get crits() {
                var e, a = (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.crits) || 0;
                return "function" === typeof a && (a = a(this.unit)),
                a
            }
            get damageM() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.damageM) || 0
            }
            get shiftM() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.shiftM) || 0
            }
            get damageMax() {
                return Number(this.damage || 0) + Number(this.damageAdj || 0)
            }
            get rangePB() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.rangePB) || ""
            }
            get rangeS() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.rangeS) || ""
            }
            get rangeM() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.rangeM) || ""
            }
            get rangeL() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.rangeL) || ""
            }
            get rangeX() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.rangeX) || ""
            }
            get varPBSdamage() {
                var e, a, t = (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.varPBSdamage) || 0;
                return t = Number(t),
                !0 === this.name.includes("SNPPC") && (null === (a = this.unit) || void 0 === a ? void 0 : a.hasPPCCapacitor(this.location)) > 0 && (t += 5),
                t
            }
            get varMdamage() {
                var e, a, t = (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.varMdamage) || 0;
                return t = Number(t),
                !0 === this.name.includes("SNPPC") && (null === (a = this.unit) || void 0 === a ? void 0 : a.hasPPCCapacitor(this.location)) > 0 && (t += 5),
                t
            }
            get varLXdamage() {
                var e, a, t = (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.varLXdamage) || 0;
                return t = Number(t),
                !0 === this.name.includes("SNPPC") && (null === (a = this.unit) || void 0 === a ? void 0 : a.hasPPCCapacitor(this.location)) > 0 && (t += 5),
                t
            }
            get useH() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.useH) || !1
            }
            get useC() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.useC) || !1
            }
            get useR() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.useR) || !1
            }
            get useAmmo() {
                var e;
                return (null === (e = g.Data[this.id]) || void 0 === e ? void 0 : e.useAmmo) || ""
            }
            get usesPrecisionAmmo() {
                return "AC" === this.useAmmo
            }
            get hasAmmoOption() {
                return "AC" === this.useAmmo
            }
            get ammo() {
                return this._ammo || p.AmmoTypeEnum.Std
            }
            set ammo(e) {
                e && Object.values(p.AmmoTypeEnum).includes(e) && (this._ammo = e)
            }
            get useTC() {
                var e, a;
                return (null === (e = this.unit) || void 0 === e ? void 0 : e.isEquipedWith("tc")) && (null === (a = g.Data[this.id]) || void 0 === a ? void 0 : a.useTC) || !1
            }
            get useOS() {
                return this._useOS || this.useSpecial("os")
            }
            set useOS(e) {
                this._useOS = e
            }
            get useAES() {
                var e;
                return !(null === (e = this.unit) || void 0 === e || !e.isEquipedWith("aes")) && this.unit.equipment.some(e => "aes" === e.id && e.location === this.location && ["LA", "RA"].includes(e.location))
            }
            get arc() {
                return this.unit.weaponArc(this.location) || A.WeaponArcEnum.Any
            }
            useFCS(e) {
                var a, t, n;
                return (null === (a = this.unit) || void 0 === a ? void 0 : a.isEquipedWith(e)) && (null === (t = g.Data[this.id]) || void 0 === t || null === (n = t.useFCS) || void 0 === n ? void 0 : n.indexOf(e)) >= 0 || !1
            }
            useSpecial(e) {
                var a, t;
                return this.id && (null === (a = g.Data[this.id]) || void 0 === a || null === (t = a.specials) || void 0 === t ? void 0 : t.indexOf(e)) >= 0 || !1
            }
            static sort(e, a) {
                const t = new p(e.unit,e)
                  , n = new p(a.unit,a);
                if (t.tic < n.tic)
                    return -1;
                if (t.tic > n.tic)
                    return 1;
                var s = Number(t.rangeX || 9)
                  , r = Number(n.rangeX || 9);
                return s < r ? -1 : s > r ? 1 : (s = Number(t.rangeL || 9)) < (r = Number(n.rangeL || 9)) ? -1 : s > r ? 1 : (s = Number(t.rangeM || 9)) < (r = Number(n.rangeM || 9)) ? -1 : s > r ? 1 : (s = Number(t.rangeS || 9)) < (r = Number(n.rangeS || 9)) ? -1 : s > r || (s = Number(t.damageMax)) < (r = Number(n.damageMax)) ? 1 : s > r || (s = Number(t.heat)) < (r = Number(n.heat)) ? -1 : s > r ? 1 : (s = t.name.toLowerCase()) < (r = n.name.toLowerCase()) ? -1 : s > r ? 1 : (s = t.arc === A.WeaponArcEnum.Rear,
                r = n.arc === A.WeaponArcEnum.Rear,
                s && !r ? 1 : !s && r ? -1 : 0)
            }
            static sortV5(e, a) {
                const t = new p(e.unit,e)
                  , n = new p(a.unit,a);
                if (t.tic < n.tic)
                    return -1;
                if (t.tic > n.tic)
                    return 1;
                var s = Number(t.rangeX || 9)
                  , r = Number(n.rangeX || 9);
                if (s < r)
                    return -1;
                if (s > r)
                    return 1;
                if ((s = Number(t.rangeL || 9)) < (r = Number(n.rangeL || 9)))
                    return -1;
                if (s > r)
                    return 1;
                if ((s = Number(t.rangeM || 9)) < (r = Number(n.rangeM || 9)))
                    return -1;
                if (s > r)
                    return 1;
                if ((s = Number(t.rangeS || 9)) < (r = Number(n.rangeS || 9)))
                    return -1;
                if (s > r)
                    return 1;
                if ((s = Number(t.damageMax)) < (r = Number(n.damageMax)))
                    return 1;
                if (s > r)
                    return -1;
                if ((s = Number(t.heat)) < (r = Number(n.heat)))
                    return -1;
                if (s > r)
                    return 1;
                const i = e => "LA" === e ? 0 : "RA" === e ? 1 : 2;
                return (s = i(t.location)) < (r = i(n.location)) ? -1 : s > r ? 1 : (s = t.name.toLowerCase()) < (r = n.name.toLowerCase()) ? -1 : s > r ? 1 : (s = t.arc === A.WeaponArcEnum.Rear,
                r = n.arc === A.WeaponArcEnum.Rear,
                s && !r ? 1 : !s && r ? -1 : 0)
            }
            static groupData(e) {
                const a = e.weapons;
                var t = {
                    name: "",
                    damage: "",
                    heat: "",
                    location: "",
                    rangePB: "",
                    rangeS: "",
                    rangeM: "",
                    rangeL: "",
                    rangeX: ""
                };
                if (!a || 0 === a.length || 1 === a.length && !a[0].id)
                    return t;
                var n = {
                    names: {},
                    locs: {},
                    heat: 0,
                    damage: 0,
                    damageM: 0,
                    shiftM: 0,
                    damageMax: 0,
                    damageC: 0,
                    useC: 0,
                    useR: 0,
                    useH: 0,
                    useM: 0,
                    useVarC: 0,
                    varPBS: 0,
                    varM: 0,
                    varLX: 0,
                    hagBase: 0,
                    flechetteLostDamage: 0
                };
                for (let l = 0; l < a.length; l++) {
                    let e = a[l];
                    if (e.id) {
                        if (n.names[e.name] ? n.names[e.name] += 1 : n.names[e.name] = 1,
                        e.useSpecial("hag20") && (n.hagBase = 2),
                        e.useSpecial("hag30") && (n.hagBase = 3),
                        e.useSpecial("hag40") && (n.hagBase = 4),
                        n.damageMax += Number(e.damageMax),
                        e.damageM > 0) {
                            let a = Math.ceil(Number(e.damageMax) / 3) - Number(e.damageM);
                            n.useM += Math.ceil(a / 3),
                            n.useM += Number(e.shiftM),
                            e.useSpecial("var") ? (n.varPBS += Number(e.varPBSdamage),
                            n.varM += Number(e.varMdamage),
                            n.varLX += Number(e.varLXdamage)) : (n.damageM += Number(e.damageM),
                            n.damageM -= Number(e.shiftM),
                            e.useSpecial("zerobase") && (n.damageM = 0))
                        } else if (e.useSpecial("var"))
                            e.useC && n.useVarC++,
                            n.varPBS += Number(e.varPBSdamage),
                            n.varM += Number(e.varMdamage),
                            n.varLX += Number(e.varLXdamage);
                        else {
                            var s = Number(e.damage);
                            if (e.hasAmmoOption && "Flechette" === e.ammo) {
                                var r = Math.floor(s / 2);
                                n.flechetteLostDamage += s - r,
                                s = r
                            }
                            n.damage += s,
                            e.useC && (n.damageC += s,
                            n.useC++)
                        }
                        n.useH += Number(e.useH),
                        n.heat += Number(e.heat),
                        n.locs[e.location] ? n.locs[e.location] += 1 : n.locs[e.location] = 1,
                        t.rangePB = "" === t.rangePB || e.rangePB > t.rangePB ? Number(e.rangePB) : Number(t.rangePB),
                        t.rangeS = "" === t.rangeS || e.rangeS > t.rangeS ? Number(e.rangeS) : Number(t.rangeS),
                        t.rangeM = "" === t.rangeM || e.rangeM > t.rangeM ? Number(e.rangeM) : Number(t.rangeM),
                        t.rangeL = "" === t.rangeL || e.rangeL > t.rangeL ? Number(e.rangeL) : Number(t.rangeL),
                        t.rangeX = "" === t.rangeX || e.rangeX > t.rangeX ? Number(e.rangeX) : Number(t.rangeX)
                    }
                }
                if (Object.keys(n.names).forEach(e => {
                    let a = (n.names[e] > 1 ? "x" + n.names[e] + " " : "") + e;
                    t.name += 0 === t.name.length ? a : ", " + a
                }
                ),
                e.useTC && t.name.length > 0 && (t.name += " (TC)"),
                e.useAIV && t.name.length > 0 && (t.name += " (AIV)"),
                e.useAV && t.name.length > 0 && (t.name += " (AV)"),
                e.useApollo && t.name.length > 0 && (t.name += " (Apollo)"),
                e.useOS && t.name.length > 0 && (t.name += " (OS)"),
                e.useAES && t.name.length > 0 && (t.name += " (AES)"),
                e.useAI && t.name.length > 0 && (t.name += " (AI)"),
                e.useR && t.name.length > 0 && (t.name += " (RF)"),
                e.useATM && t.name.length > 0 && (t.name += " (AIV)"),
                e.usePrecisionAmmo && t.name.length > 0 && (t.name += " (Precision)"),
                e.useAPAmmo && t.name.length > 0 && (t.name += " (Armor Piercing)"),
                e.useFlakAmmo && t.name.length > 0 && (t.name += " (Flak)"),
                e.useFlechetteAmmo && t.name.length > 0 && (t.name += " (Flechette)"),
                e.useTracerAmmo && t.name.length > 0 && (t.name += " (Tracer)"),
                n.useVarC > 0)
                    n.varPBS = Math.ceil(n.varPBS / 3) - n.useVarC,
                    n.varM = Math.ceil(n.varM / 3) - n.useVarC,
                    n.varLX = Math.ceil(n.varLX / 3) - n.useVarC,
                    n.hagBase > 0 ? t.damage = n.hagBase + "+C" + n.varPBS + "|" + n.varM + "|" + n.varLX : t.damage = n.useVarC + "+C" + n.varPBS + "|" + n.varM + "|" + n.varLX;
                else if (n.damageC = Math.ceil(n.damageC / 3) - n.useC,
                n.varPBS || n.varM || n.varLX ? (n.varPBS = Math.ceil((n.damage + n.varPBS) / 3) + n.damageM - n.damageC,
                n.varM = Math.ceil((n.damage + n.varM) / 3) + n.damageM - n.damageC,
                n.varLX = Math.ceil((n.damage + n.varLX) / 3) + n.damageM - n.damageC,
                t.damage = n.varPBS + "|" + n.varM + "|" + n.varLX) : t.damage = Math.ceil(n.damage / 3) + n.damageM - n.damageC,
                n.useC > 0 && (t.damage += "+C" + n.damageC),
                n.useH > 0 && (t.damage += "+H" + Math.max(Math.round(n.useH / 5), 1)),
                n.useM > 0 && (t.damage += "+M" + n.useM + " (" + Math.ceil(n.damageMax / 3) + ")"),
                n.flechetteLostDamage > 0 && "number" === typeof t.damage) {
                    var i = Math.ceil((n.damage + n.flechetteLostDamage) / 3) + n.damageM - n.damageC - t.damage;
                    i > 0 && (t.damage = t.damage + " (" + i + " + AI)")
                }
                return t.heat = Math.round(n.heat / 5),
                Object.keys(n.locs).forEach(e => {
                    t.location += 0 === t.location.length ? e : ", " + e
                }
                ),
                t.location.indexOf("(R)") >= 0 && (t.location = t.location.replaceAll("(R) ", ""),
                t.location = "(R) " + t.location.trim()),
                (e.useTC || e.useApollo || e.useAES) && (t.rangePB--,
                t.rangeS--,
                t.rangeM--,
                t.rangeL--,
                t.rangeX--),
                e.usePrecisionAmmo && (t.rangePB--,
                t.rangeS--,
                t.rangeM--,
                t.rangeL--,
                t.rangeX--),
                e.useAPAmmo && (t.rangePB++,
                t.rangeS++,
                t.rangeM++,
                t.rangeL++,
                t.rangeX++),
                t.rangePB >= 0 && (t.rangePB = t.rangePB > 6 ? "--" : "+" + t.rangePB),
                t.rangeS >= 0 && (t.rangeS = t.rangeS > 6 ? "--" : "+" + t.rangeS),
                t.rangeM >= 0 && (t.rangeM = t.rangeM > 6 ? "--" : "+" + t.rangeM),
                t.rangeL >= 0 && (t.rangeL = t.rangeL > 6 ? "--" : "+" + t.rangeL),
                t.rangeX >= 0 && (t.rangeX = t.rangeX > 6 ? "--" : "+" + t.rangeX),
                t
            }
        }
        p.AmmoTypeEnum = Object.freeze({
            Std: "Std",
            Precision: "Precision",
            AP: "AP",
            Flak: "Flak",
            Flechette: "Flechette",
            Tracer: "Tracer"
        });
        const y = p;
        class x {
            constructor() {
                this.weapons = [],
                Object.seal(this)
            }
            get used() {
                return this.weapons.length > 0
            }
            get rawdamage() {
                var e = 0;
                return this.weapons.forEach(a => {
                    e += Number(a.damage),
                    e += Number(a.damageAdj)
                }
                ),
                e
            }
            get damage() {
                var e = 0;
                return this.weapons.forEach(a => {
                    !a.damageM > 0 && (e += Number(a.damage)),
                    a.damageM > 0 && a.useSpecial("var") && (e += Number(a.varPBSdamage))
                }
                ),
                e
            }
            get damageM() {
                var e = 0;
                return this.weapons.forEach(a => {
                    a.damageM > 0 && !a.useSpecial("var") && (e += Number(a.damageM),
                    e -= Number(a.shiftM))
                }
                ),
                e
            }
            get damageBase() {
                var e = 0;
                for (let a = 0; a < this.weapons.length; a++)
                    if (this.weapons[a].damageM > 0) {
                        let t = Math.ceil(Number(this.weapons[a].damageMax) / 3) - Number(this.weapons[a].damageM);
                        Math.ceil(t / 3) + (this.weapons[a].useSpecial("extraM") ? 1 : 0),
                        Number(this.weapons[a].shiftM),
                        e += Number(this.weapons[a].damageM),
                        e -= Number(this.weapons[a].shiftM)
                    } else
                        e += Math.ceil(Number(this.weapons[a].damage) / 3);
                return e
            }
            get heat() {
                var e = 0;
                return this.weapons.forEach(a => {
                    e += Number(a.heat)
                }
                ),
                e
            }
            get rangePB() {
                var e = null;
                return this.weapons.forEach(a => {
                    (null === e || a.rangePB > e) && (e = Number(a.rangePB))
                }
                ),
                e
            }
            get rangeS() {
                var e = null;
                return this.weapons.forEach(a => {
                    (null === e || a.rangeS > e) && (e = Number(a.rangeS))
                }
                ),
                e
            }
            get rangeM() {
                var e = null;
                return this.weapons.forEach(a => {
                    (null === e || a.rangeM > e) && (e = Number(a.rangeM))
                }
                ),
                e
            }
            get rangeL() {
                var e = null;
                return this.weapons.forEach(a => {
                    (null === e || a.rangeL > e) && (e = Number(a.rangeL))
                }
                ),
                e
            }
            get rangeX() {
                var e = null;
                return this.weapons.forEach(a => {
                    (null === e || a.rangeX > e) && (e = Number(a.rangeX))
                }
                ),
                e
            }
            get useR() {
                var e = 0;
                return this.weapons.forEach(a => {
                    !a.damageM > 0 && (e += Number(a.useR))
                }
                ),
                e
            }
            get arcs() {
                var e = [];
                return this.weapons.forEach(a => {
                    e.includes(a.arc) || e.push(a.arc)
                }
                ),
                e
            }
            get useTC() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useTC)) || !1
            }
            get useAIV() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useFCS("aiv"))) || !1
            }
            get useAV() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useFCS("av"))) || !1
            }
            get useApollo() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useFCS("apollo"))) || !1
            }
            get useSSRM() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("ssrm"))) || !1
            }
            get useSLRM() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("slrm"))) || !1
            }
            get useSRM() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("srm"))) || !1
            }
            get useLRM() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("lrm"))) || !1
            }
            get useMRM() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("mrm"))) || !1
            }
            get useATM() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("atm"))) || !1
            }
            get useRL() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("rl"))) || !1
            }
            get useSRT() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("srt"))) || !1
            }
            get useLRT() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("lrt"))) || !1
            }
            get useHAG() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("hag"))) || !1
            }
            get useSBG() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useSpecial("sbg"))) || !1
            }
            get useOS() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useOS)) || !1
            }
            get useAES() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.every(e => e.useAES)) || !1
            }
            get usePrecisionAmmo() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.length) > 0 && this.weapons.every(e => e.hasAmmoOption && "Precision" === e.ammo)
            }
            get ammoType() {
                if (!this.weapons || 0 === this.weapons.length)
                    return "Std";
                const e = this.weapons.filter(e => e.hasAmmoOption);
                if (0 === e.length)
                    return "Std";
                const a = new Set(e.map(e => e.ammo));
                return 1 === a.size ? a.values().next().value : "Std"
            }
            get useAPAmmo() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.length) > 0 && this.weapons.every(e => e.hasAmmoOption && "AP" === e.ammo)
            }
            get useFlakAmmo() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.length) > 0 && this.weapons.every(e => e.hasAmmoOption && "Flak" === e.ammo)
            }
            get useFlechetteAmmo() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.some(e => e.hasAmmoOption && "Flechette" === e.ammo)) || !1
            }
            get useTracerAmmo() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.some(e => e.hasAmmoOption && "Tracer" === e.ammo)) || !1
            }
            get useAI() {
                var e;
                return (null === (e = this.weapons) || void 0 === e ? void 0 : e.some(e => e.useSpecial("ai") || e.hasAmmoOption && "Flechette" === e.ammo)) || !1
            }
        }
        x.GroupNumbers = Object.freeze([1, 2, 3, 4, 5, 6, 7, 8, 9]);
        class v {
            constructor(e) {
                if (this._blank = !1,
                this._chassis = "",
                this._clanname = "",
                this._variant = "",
                this._motiveType = null,
                this._movePoints = 0,
                this._locations = [],
                this._armor = {},
                this._structure = {},
                this._weapons = [],
                this._equipment = [],
                this._tech = v.TechEnum.IS,
                this._omni = !1,
                this._showOmittedEquipment = !1,
                new.target === v)
                    throw new TypeError('Cannot construct instances of class "AbstractUnit".');
                if (e) {
                    if (!(e instanceof v))
                        throw new TypeError(e.constructor.name + ' is not a sub-class of "AbstractUnit"');
                    this.isBlank = e.isBlank,
                    this._type = e.type
                }
            }
            get type() {
                return this._type
            }
            set type(e) {
                e && e !== this._type && (this._type = e,
                this._chassis = "",
                this._variant = "",
                this._tonnage = this.allowedTonnage[0],
                this._locations = [],
                this._armor = {},
                this._weapons = [],
                this._equipment = [])
            }
            get chassis() {
                return this._chassis
            }
            set chassis(e) {
                this._chassis !== e && (this._chassis = e)
            }
            get clanname() {
                return this._clanname
            }
            set clanname(e) {
                this._clanname !== e && (this._clanname = e)
            }
            get variant() {
                return this._variant
            }
            set variant(e) {
                this._variant !== e && (this._variant = e)
            }
            get isOmni() {
                return this._omni
            }
            set isOmni(e) {
                this._omni !== !!e && (this._omni = !!e)
            }
            get isBlank() {
                return this._blank
            }
            set isBlank(e) {
                this._blank !== !!e && (this._blank = !!e)
            }
            get showOmittedEquipment() {
                return this._showOmittedEquipment
            }
            set showOmittedEquipment(e) {
                this._showOmittedEquipment !== !!e && (this._showOmittedEquipment = !!e)
            }
            get tonnage() {
                return this._tonnage || ""
            }
            set tonnage(e) {
                if (!isNaN(+e))
                    if (this.allowedTonnage.includes(+e))
                        this._tonnage = +e;
                    else {
                        const a = this.allowedTonnage.find(a => a >= +e);
                        this._tonnage = null !== a && void 0 !== a ? a : this.allowedTonnage[this.allowedTonnage.length - 1]
                    }
            }
            get tech() {
                return this._tech
            }
            set tech(e) {
                if (e && Object.values(v.TechEnum).includes(e) && (this._tech = e),
                this.tech !== v.TechEnum.Mixed) {
                    var a = []
                      , t = [];
                    this.weapons.forEach( (e, t) => {
                        e.tech !== v.TechEnum.Mixed && e.tech !== this.tech && a.push(t)
                    }
                    ),
                    this.equipment.forEach( (e, a) => {
                        e.tech !== v.TechEnum.Mixed && e.tech !== this.tech && t.push(a)
                    }
                    );
                    for (var n = a.length - 1; n >= 0; n--)
                        this.weapons.splice(a[n], 1);
                    for (var s = t.length - 1; s >= 0; s--)
                        this.equipment.splice(t[s], 1)
                }
            }
            get armor() {
                return this._armor
            }
            set armor(e) {
                Object.keys(e).forEach(a => e[a] = +e[a]),
                this._armor = e
            }
            get structure() {
                return this._structure
            }
            get weapons() {
                return this._weapons
            }
            set weapons(e) {
                this._weapons = e
            }
            get equipment() {
                return this._equipment
            }
            set equipment(e) {
                this._equipment = e
            }
            get locations() {
                return this._locations
            }
            set locations(e) {
                e && e !== this._locations && (this._locations = e,
                this._weapons.forEach(e => {
                    this._locations.includes(e.location) || (e.location = "")
                }
                ),
                this._equipment.forEach(e => {
                    this._locations.includes(e.location) || (e.location = "")
                }
                ))
            }
            get fixedTonnage() {
                return Math.min(5 * Math.floor((this.tonnage || 0) / 5), 100)
            }
            get tics() {
                var e = new Array(9);
                for (let a = 0; a < e.length; a++)
                    e[a] = new x;
                return this.weapons.forEach(a => {
                    a.tic && e[a.tic - 1].weapons.push(a)
                }
                ),
                e
            }
            isImportSupported(e) {
                var a, t;
                return !(!Object.getOwnPropertyNames(v.ImportTypeEnum).includes(e) && !Object.values(v.ImportTypeEnum).includes(e)) && ((null === (a = this.supportedImports) || void 0 === a ? void 0 : a.includes(e)) || (null === (t = this.supportedImports) || void 0 === t ? void 0 : t.includes(v.ImportTypeEnum[e])))
            }
            isEquipedWith(e) {
                var a;
                return !!e && (null === (a = this.equipment) || void 0 === a ? void 0 : a.some(a => a.id === e.toLowerCase()))
            }
            isEquipedWithCount(e) {
                var a, t = 0;
                e && (null === (a = this.equipment) || void 0 === a || a.forEach(a => {
                    a.id === e.toLowerCase() && t++
                }
                ));
                return t
            }
            hasEquipment(e) {
                var a;
                return e && e.id ? null === (a = this.equipment) || void 0 === a ? void 0 : a.some(a => a.id === e.id && (!e.hasLoc || a.location === e.location) && (!e.subtypes || a.subtype === e.subtype)) : this.isEquipedWith(e)
            }
            hasPPCCapacitor(e) {
                var a, t = 0;
                e && (null === (a = this.equipment) || void 0 === a || a.forEach(a => {
                    "ppccapacitor" === a.id && a.location === e && (t = 1)
                }
                ));
                return t
            }
            getEquipment(e) {
                if (this.hasEquipment(e)) {
                    "string" === typeof e && (e = new d({
                        id: e
                    }));
                    for (const a in this.equipment)
                        if (this.equipment[a].id === e.id && (!e.hasLoc || this.equipment[a].location === e.location) && (!e.subtypes || this.equipment[a].subtype === e.subtype))
                            return this.equipment[a]
                }
            }
            addWeapon(e) {
                if (e)
                    e.unit = this;
                else {
                    e = new y(this);
                    let a = this.tics
                      , t = 1;
                    for (let e = 0; e < a.length; e++)
                        if (0 === a[e].weapons.length) {
                            t = e + 1;
                            break
                        }
                    e.tic = t
                }
                this.weapons.push(e)
            }
            addEquipment(e) {
                e || (e = new d),
                this.equipment.push(e)
            }
            removeWeapon(e) {
                var a;
                const t = null === (a = this.weapons[e]) || void 0 === a ? void 0 : a.tic;
                this.weapons.splice(e, 1),
                0 === this.tics[t - 1].weapons.length && this.weapons.forEach(e => {
                    e.tic > t && (e.tic -= 1)
                }
                )
            }
            removeEquipment(e) {
                this.equipment.splice(e, 1)
            }
            changeWeapon(e, a, t) {
                if (this.weapons[e][a] = t,
                "ammo" === a && ["Precision", "AP", "Flak"].includes(t)) {
                    const a = Number(this.weapons[e].tic);
                    this.weapons.forEach( (n, s) => {
                        s !== Number(e) && Number(n.tic) === a && n.hasAmmoOption && (n._ammo = t)
                    }
                    )
                }
            }
            changeEquipment(e, a, t) {
                this.equipment[e][a] = t
            }
            sortWeapons() {
                this.weapons.sort( (e, a) => y.sort(e, a))
            }
            autoGroupWeapons() {
                var e = new Array(9);
                for (let a = 0; a < e.length; a++)
                    e[a] = new x;
                this.weapons.forEach(e => {
                    e.tic = 1
                }
                ),
                this.sortWeapons(),
                this.weapons.forEach(a => {
                    var t = [];
                    for (let s = 0; s < 9; s++) {
                        if (t[s] = 100 - s,
                        !e[s].used)
                            continue;
                        if (a.arc === v.WeaponArcEnum.Rear && !e[s].arcs.includes(v.WeaponArcEnum.Rear)) {
                            t[s] = 0;
                            continue
                        }
                        if (a.arc === v.WeaponArcEnum.Left && !e[s].arcs.includes(v.WeaponArcEnum.Left)) {
                            t[s] = 0;
                            continue
                        }
                        if (a.arc === v.WeaponArcEnum.Right && !e[s].arcs.includes(v.WeaponArcEnum.Right)) {
                            t[s] = 0;
                            continue
                        }
                        if (this.isEquipedWith("tc") && a.useTC !== e[s].useTC) {
                            t[s] = 0;
                            continue
                        }
                        if (this.isEquipedWith("aiv") && a.useFCS("aiv") !== e[s].useAIV) {
                            t[s] = 0;
                            continue
                        }
                        if (this.isEquipedWith("av") && a.useFCS("av") !== e[s].useAV) {
                            t[s] = 0;
                            continue
                        }
                        if (this.isEquipedWith("apollo") && a.useFCS("apollo") !== e[s].useApollo) {
                            t[s] = 0;
                            continue
                        }
                        if (this.isEquipedWith("aes") && a.useAES !== e[s].useAES) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("ssrm") !== e[s].useSSRM) {
                            t[s] = 0;
                            continue
                        }
                        if (Number(a.useR) > 0 && 0 === e[s].useR || 0 === Number(a.useR) && e[s].useR > 0) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("slrm") !== e[s].useSLRM) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("srm") !== e[s].useSRM) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("lrm") !== e[s].useLRM) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("mrm") !== e[s].useMRM) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("atm") !== e[s].useATM) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("rl") !== e[s].useRL) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("srt") !== e[s].useSRT) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("lrt") !== e[s].useLRT) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("hag") !== e[s].useHAG) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useSpecial("sbg") !== e[s].useSBG) {
                            t[s] = 0;
                            continue
                        }
                        if (a.useOS !== e[s].useOS) {
                            t[s] = 0;
                            continue
                        }
                        if ("P" === a.type) {
                            t[s] = 0;
                            continue
                        }
                        let n = 0;
                        if (n = a.damageM > 0 ? Math.ceil(e[s].damage / 3) + e[s].damageM + Number(a.damageM) : Math.ceil((e[s].damage + Number(a.damage)) / 3) + e[s].damageM,
                        this.squadSize && (n *= this.squadSize),
                        n > 5)
                            t[s] = 0;
                        else if (e[s].arcs.includes(a.arc) || (t[s] *= .6),
                        t[s] *= Number(e[s].rangeX) === Number(a.rangeX) ? 1 : .1,
                        t[s] *= Number(e[s].rangeL) === Number(a.rangeL) ? 1 : .2,
                        t[s] *= Number(e[s].rangeM) === Number(a.rangeM) ? 1 : .4,
                        t[s] *= Number(e[s].rangeS) === Number(a.rangeS) ? 1 : .8,
                        this.destinySinks) {
                            const n = Math.round((e[s].heat + Number(a.heat)) / 5) - this.destinySinks;
                            t[s] *= 1 - .2 * Math.min(Math.max(n, 0), 5)
                        }
                    }
                    var n = 0;
                    for (let e = 0; e < 9; e++)
                        t[e] > t[n] && (n = e);
                    a.tic = n + 1,
                    e[n].weapons.push(a)
                }
                )
            }
            _scoreWeaponForTicV5(e, a, t) {
                let n = 100 - t;
                if (!a.used)
                    return n;
                if (e.arc === v.WeaponArcEnum.Rear && !a.arcs.includes(v.WeaponArcEnum.Rear))
                    return 0;
                if (e.arc === v.WeaponArcEnum.Left && !a.arcs.includes(v.WeaponArcEnum.Left))
                    return 0;
                if (e.arc === v.WeaponArcEnum.Right && !a.arcs.includes(v.WeaponArcEnum.Right))
                    return 0;
                if (this.isEquipedWith("tc") && e.useTC !== a.useTC)
                    return 0;
                if (this.isEquipedWith("aiv") && e.useFCS("aiv") !== a.useAIV)
                    return 0;
                if (this.isEquipedWith("av") && e.useFCS("av") !== a.useAV)
                    return 0;
                if (this.isEquipedWith("apollo") && e.useFCS("apollo") !== a.useApollo)
                    return 0;
                if (this.isEquipedWith("aes") && e.useAES !== a.useAES)
                    return 0;
                if (e.useSpecial("ssrm") !== a.useSSRM)
                    return 0;
                if (Number(e.useR) > 0 && 0 === a.useR || 0 === Number(e.useR) && a.useR > 0)
                    return 0;
                if (e.useSpecial("slrm") !== a.useSLRM)
                    return 0;
                if (e.useSpecial("srm") !== a.useSRM)
                    return 0;
                if (e.useSpecial("lrm") !== a.useLRM)
                    return 0;
                if (e.useSpecial("mrm") !== a.useMRM)
                    return 0;
                if (e.useSpecial("atm") !== a.useATM)
                    return 0;
                if (e.useSpecial("rl") !== a.useRL)
                    return 0;
                if (e.useSpecial("srt") !== a.useSRT)
                    return 0;
                if (e.useSpecial("lrt") !== a.useLRT)
                    return 0;
                if (e.useSpecial("hag") !== a.useHAG)
                    return 0;
                if (e.useSpecial("sbg") !== a.useSBG)
                    return 0;
                if (e.useOS !== a.useOS)
                    return 0;
                if ("P" === e.type)
                    return 0;
                let s = 0;
                if (s = e.damageM > 0 ? Math.ceil(a.damage / 3) + a.damageM + Number(e.damageM) : Math.ceil((a.damage + Number(e.damage)) / 3) + a.damageM,
                this.squadSize && (s *= this.squadSize),
                s > 5)
                    return 0;
                if (a.arcs.includes(e.arc)) {
                    if (e.arc === v.WeaponArcEnum.Any && a.weapons.length > 0) {
                        new Set(a.weapons.map(e => e.location)).has(e.location) || (n *= .8)
                    }
                } else {
                    a.arcs.every(e => e === v.WeaponArcEnum.Any) && e.arc === v.WeaponArcEnum.Front ? n *= .8 : n *= .6
                }
                n *= Number(a.rangeX) === Number(e.rangeX) ? 1 : .1,
                n *= Number(a.rangeL) === Number(e.rangeL) ? 1 : .2,
                n *= Number(a.rangeM) === Number(e.rangeM) ? 1 : .4,
                n *= Number(a.rangeS) === Number(e.rangeS) ? 1 : .8;
                const r = e.usesPrecisionAmmo
                  , i = a.weapons.some(e => e.usesPrecisionAmmo)
                  , l = a.weapons.some(e => !e.usesPrecisionAmmo);
                (r && l || !r && i) && (n *= .8);
                const o = Math.round((a.heat + Number(e.heat)) / 5)
                  , m = Math.round(a.heat / 5) + Math.round(Number(e.heat) / 5)
                  , c = m - o;
                let u = 0
                  , h = 0;
                if (!(e.damageM > 0)) {
                    const t = Math.ceil((a.damage + Number(e.damage)) / 3);
                    h = Math.ceil(a.damage / 3) + Math.ceil(Number(e.damage) / 3),
                    u = h - t
                }
                if (c > 0 && m > 0) {
                    let e = Math.min(m / Math.max(o, 1), 2);
                    u > 0 && h > 0 && (e = 1 + (e - 1) * Math.max(1 - u / h, 0)),
                    n *= e
                } else
                    u > 0 && h > 0 && (n *= Math.max(1 - u / h, .1));
                if (this.destinySinks) {
                    const t = Math.round((a.heat + Number(e.heat)) / 5) - this.destinySinks;
                    n *= 1 - .2 * Math.min(Math.max(t, 0), 5)
                }
                return n
            }
            autoGroupWeaponsV5() {
                var e = this;
                var a = new Array(9);
                for (let n = 0; n < a.length; n++)
                    a[n] = new x;
                this.weapons.forEach(e => {
                    e.tic = 1
                }
                ),
                this.weapons.sort( (e, a) => y.sortV5(e, a));
                const t = function(n, s) {
                    let r = arguments.length > 2 && void 0 !== arguments[2] ? arguments[2] : -1;
                    var i = [];
                    for (let t = 0; t < 9; t++)
                        i[t] = e._scoreWeaponForTicV5(n, a[t], t);
                    var l = 0;
                    for (let e = 0; e < 9; e++)
                        i[e] > i[l] && (l = e);
                    let o = null;
                    if (s < 3)
                        for (let t = 0; t < 9; t++)
                            if (a[t].used && !(a[t].weapons.length < 2) && t !== r)
                                for (let s = 0; s < a[t].weapons.length; s++) {
                                    const r = a[t].weapons.splice(s, 1)[0]
                                      , m = e._scoreWeaponForTicV5(n, a[t], t);
                                    a[t].weapons.splice(s, 0, r),
                                    m > i[l] && (!o || m > o.score) && (o = {
                                        ticIdx: t,
                                        weaponIdx: s,
                                        score: m
                                    })
                                }
                    if (o) {
                        const e = a[o.ticIdx].weapons.splice(o.weaponIdx, 1)[0];
                        n.tic = o.ticIdx + 1,
                        a[o.ticIdx].weapons.push(n),
                        t(e, s + 1, o.ticIdx)
                    } else
                        n.tic = l + 1,
                        a[l].weapons.push(n)
                };
                this.weapons.forEach(e => {
                    t(e, 0)
                }
                )
            }
            sortEquipment() {
                this.equipment.sort( (e, a) => d.sort(e, a))
            }
            validateWeapons(e) {
                var a = {};
                this.tics.forEach(e => {
                    var t = Math.ceil(e.damage / 3) + e.damageM
                      , n = Math.ceil(e.rawdamage / 3);
                    this.squadSize && (t *= this.squadSize),
                    a.maxDamage = a.maxDamage || e.weapons.length > 1 && (n > 14 || t > 5),
                    a.groupRear = a.groupRear || e.arcs.includes(v.WeaponArcEnum.Rear) && e.arcs.length > 1,
                    a.groupSides = a.groupSides || (e.arcs.includes(v.WeaponArcEnum.Left) || e.arcs.includes(v.WeaponArcEnum.Right)) && e.arcs.length > 1,
                    e.weapons.forEach(t => {
                        a.groupFCS = a.groupFCS || e.useAIV && !t.useFCS("aiv") && t.damageM,
                        a.groupFCS = a.groupFCS || e.useAV && !t.useFCS("av") && t.damageM > 0,
                        a.groupStreak = a.groupStreak || e.useSSRM !== t.useSpecial("ssrm") || e.useSLRM !== t.useSpecial("slrm"),
                        a.groupLRM = a.groupLRM || e.useLRM !== t.useSpecial("lrm"),
                        a.groupSRM = a.groupSRM || e.useSRM !== t.useSpecial("srm"),
                        a.groupMRM = a.groupMRM || e.useMRM !== t.useSpecial("mrm"),
                        a.groupATM = a.groupATM || e.useATM !== t.useSpecial("atm"),
                        a.groupRL = a.groupRL || e.useRL !== t.useSpecial("rl"),
                        a.groupSRT = a.groupSRT || e.useSRT !== t.useSpecial("srt"),
                        a.groupLRT = a.groupLRT || e.useLRT !== t.useSpecial("lrt"),
                        a.groupR = a.groupR || Number(t.useR) > 0 && 0 === e.useR || 0 === Number(t.useR) && e.useR > 0,
                        a.groupHAG = a.groupHAG || e.useHAG !== t.useSpecial("hag"),
                        a.groupSBG = a.groupSBG || e.useSBG !== t.useSpecial("sbg"),
                        a.groupOS = a.groupOS || e.useOS !== t.useOS,
                        a.groupPhysical = a.groupPhysical || "P" === t.type && e.weapons.length > 1
                    }
                    );
                    const s = e.weapons.filter(e => e.hasAmmoOption);
                    if (s.length > 1) {
                        const e = new Set(s.map(e => e.ammo).filter(e => "Std" !== e));
                        a.groupAmmo = a.groupAmmo || e.size > 1
                    }
                }
                ),
                e.weapons = "",
                e.weapons += a.maxDamage ? " A single TIC with multiple weapons cannot deal more than 5 points of damage (or 14 points of max missile damage)." : "",
                e.weapons += a.groupRear ? " Rear-facing weapons can only be grouped with other rear-facing weapons." : "",
                e.weapons += a.groupSides ? " Side-facing weapons can only be grouped with other same-side-facing weapons." : "",
                e.weapons += a.groupFCS ? " Missiles equipped with an Artemis Fire Control System cannot be grouped with non-Artemis missiles." : "",
                e.weapons += a.groupStreak ? " Streak missiles can only be grouped with other Streak missiles of the same type." : "",
                e.weapons += a.groupLRM ? " Missile launchers can only be grouped with other launchers of the same type." : "",
                e.weapons += a.groupSRM ? " Missile launchers can only be grouped with other launchers of the same type." : "",
                e.weapons += a.groupMRM ? " Missile launchers can only be grouped with other launchers of the same type." : "",
                e.weapons += a.groupATM ? " Missile launchers can only be grouped with other launchers of the same type." : "",
                e.weapons += a.groupRL ? " Missile launchers can only be grouped with other launchers of the same type." : "",
                e.weapons += a.groupSRT ? " Torpedo launchers can only be grouped with other launchers of the same type." : "",
                e.weapons += a.groupLRT ? " Torpedo launchers can only be grouped with other launchers of the same type." : "",
                e.weapons += a.groupR ? " Rapid fire weapons can only be grouped with other rapid fire weapons." : "",
                e.weapons += a.groupHAG ? " Hyper-Assault Gauss can only be grouped with other Hyper-Assault Gauss." : "",
                e.weapons += a.groupSBG ? " Silver Bullet Gauss can only be grouped with other Silver Bullet Gauss." : "",
                e.weapons += a.groupOS ? " One-shot weapons can only be grouped with other one-shot weapons." : "",
                e.weapons += a.groupPhysical ? " Physical weapons cannot be grouped with any other weapon." : "",
                e.weapons += a.groupAmmo ? " AC/LAC weapons in a TIC cannot use different special ammo types." : "",
                e.weapons.length > 0 && (e.weapons = "Errors:" + e.weapons)
            }
            get supportedImports() {
                return []
            }
            get typeName() {
                return this.type
            }
            get cardName() {
                let e = this.chassis.trim();
                return this.clanname && (e = e + " (" + this.clanname.trim() + ")"),
                (e + " " + (this.variant.trim() || "")).trim().toUpperCase()
            }
            get motiveType() {
                return this._motiveType
            }
            set motiveType(e) {
                e && Object.values(this.motiveTypes).includes(e) && (this._motiveType = e)
            }
            get movePoints() {
                return this._move
            }
            set movePoints(e) {
                e && !isNaN(+e) && +e >= 0 && (this._movePoints = +e)
            }
            get allowedTonnage() {
                return [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            }
            get destinyMove() {
                return "" + this._movePoints
            }
            get destinyTMM() {
                return "" + this.tmm(this._movePoints)
            }
            get destinySinks() {
                return this.sinks || 0
            }
            get destinyWeapons() {
                const e = this.clone();
                e.sortWeapons();
                const a = e.tics;
                var t = new Array(10);
                for (let n = 0; n < a.length; n++) {
                    let e = y.groupData(a[n]);
                    e.name && (t[n] = e)
                }
                return t
            }
            get destinyEquipment() {
                var e = ""
                  , a = 0;
                return this.equipment.forEach(t => {
                    if (t.id && (!t.omit || this.showOmittedEquipment)) {
                        var n = a > 0 ? ", " : "";
                        n += t.name + (t.subtype ? ":" + t.subtype : "") + (t.location ? " (" + t.location + ")" : "") + (t.uses && t.uses > 0 ? " [" + t.uses + "]" : ""),
                        e += n,
                        a++
                    }
                }
                ),
                e
            }
            tmm(e) {
                const a = 2 * parseInt(e);
                let t = 0;
                return a >= 0 && (a < 5 ? t = 0 : a < 9 ? t = 1 : a < 13 ? t = 2 : a < 19 ? t = 3 : a < 35 ? t = 4 : a >= 35 && (t = 5)),
                t
            }
            validate() {
                var e = {};
                return this.validateWeapons(e),
                e
            }
            get motiveTypes() {
                throw new TypeError("Sub-classes must define their valid motive types.")
            }
            get destinyLocations() {
                throw new TypeError("Sub-classes must define their BT:D locations.")
            }
            clone() {
                throw new TypeError("Sub-classes must define this method.")
            }
            destinyArmorValue(e) {
                throw new TypeError("Sub-classes must define the method for calculating their BT:D armor values.")
            }
            destinyStructureValue(e) {
                throw new TypeError("Sub-classes must define the method for calculating their BT:D structure values.")
            }
            weaponArc(e) {
                throw new TypeError("Sub-classes must define their own BT:D weapon arcs.")
            }
        }
        v.TechEnum = Object.freeze({
            IS: "Inner Sphere",
            Clan: "Clan",
            Mixed: "Mixed"
        }),
        v.UnitTypeEnum = Object.freeze({
            BM: "BattleMech",
            CV: "Combat Vehicle",
            AF: "Fighter",
            BA: "Battle Armor",
            IN: "Infantry"
        }),
        v.ImportTypeEnum = Object.freeze({
            MML: "Mega Mek Lab"
        }),
        v.WeaponArcEnum = Object.freeze({
            Front: "Front",
            Rear: "Rear",
            Left: "Left",
            Right: "Right",
            Any: "Any"
        });
        const A = v;
        class M extends A {
            constructor(e) {
                var a;
                (super(e),
                this._sinks = {
                    count: 0,
                    isDHS: !1
                },
                this._walk = 0,
                this._jump = 0,
                this.type = A.UnitTypeEnum.BM,
                e instanceof M) ? (this._chassis = e.chassis,
                this._clanname = e.clanname,
                this._variant = e.variant,
                this._motiveType = e.motiveType,
                this._tonnage = e.tonnage,
                this._tech = e.tech,
                this._omni = e.isOmni,
                this._walk = e.walk,
                this._jump = e.jump,
                this._sinks = {
                    count: e.sinks,
                    isDHS: e.hasDHS
                },
                this._armor = e.armor,
                this._weapons = [],
                null === (a = e.weapons) || void 0 === a || a.forEach(e => {
                    this.addWeapon(new y(this,e))
                }
                ),
                this._equipment = e.equipment,
                this._showOmittedEquipment = e.showOmittedEquipment) : (this._motiveType = M.MotiveTypeEnum.BP,
                this._tonnage = this.allowedTonnage[0],
                this.resetArmor());
                this.resetLocations()
            }
            get typeName() {
                return this.isOmni ? "OmniMech" : "BattleMech"
            }
            get sinks() {
                var e;
                return (null === (e = this._sinks) || void 0 === e ? void 0 : e.count) || 0
            }
            set sinks(e) {
                !isNaN(+e) && +e >= 0 && (this._sinks.count = +e)
            }
            get hasDHS() {
                var e;
                return null === (e = this._sinks) || void 0 === e ? void 0 : e.isDHS
            }
            set hasDHS(e) {
                this._sinks.isDHS = !!e
            }
            get walk() {
                return this._walk
            }
            set walk(e) {
                !isNaN(+e) && +e >= 0 && (this._walk = +e)
            }
            get jump() {
                return this._jump
            }
            set jump(e) {
                !isNaN(+e) && +e >= 0 && (this._jump = +e)
            }
            get walkMP() {
                var e = Number(this.walk) || 0;
                return e > 0 && (this.isEquipedWith("masc") && this.isEquipedWith("supercharger") ? e = Math.ceil(1.5 * e) : (this.isEquipedWith("masc") || this.isEquipedWith("supercharger")) && (e = Math.ceil(1.25 * e))),
                e
            }
            get runMP() {
                return Math.max(Math.round(1.5 * this.walkMP) + (this.isEquipedWith("hardened") ? -1 : 0), 0)
            }
            get jumpMP() {
                var e = Number(this.jump) || 0;
                return e > 0 && this.isEquipedWith("partwing") && (e += this.tonnage <= 55 ? 2 : 1),
                e
            }
            resetLocations() {
                this.locations = this.motiveType === M.MotiveTypeEnum.QD ? Object.values(M.QDLocationEnum) : Object.values(M.BPLocationEnum)
            }
            resetArmor(e) {
                const a = this._armor;
                this._armor = {};
                var t = {}
                  , n = {};
                this._motiveType === M.MotiveTypeEnum.BP ? (t = M.BPArmorEnum,
                e === M.MotiveTypeEnum.QD && (n = {
                    [M.BPArmorEnum.LA]: [M.QDArmorEnum.LFL],
                    [M.BPArmorEnum.RA]: [M.QDArmorEnum.RFL],
                    [M.BPArmorEnum.LL]: [M.QDArmorEnum.LRL],
                    [M.BPArmorEnum.RL]: [M.QDArmorEnum.RRL]
                })) : this._motiveType === M.MotiveTypeEnum.QD && (t = M.QDArmorEnum,
                e === M.MotiveTypeEnum.BP && (n = {
                    [M.QDArmorEnum.LFL]: M.BPArmorEnum.LA,
                    [M.QDArmorEnum.RFL]: M.BPArmorEnum.RA,
                    [M.QDArmorEnum.LRL]: M.BPArmorEnum.LL,
                    [M.QDArmorEnum.RRL]: M.BPArmorEnum.RL
                })),
                Object.keys(t).forEach(e => {
                    const t = a[n[e] || e];
                    this._armor[e] = t || 1
                }
                )
            }
            get supportedImports() {
                return [A.ImportTypeEnum.MML]
            }
            get allowedTonnage() {
                return [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
            }
            get structure() {
                return M.STRUCTURE_DATA[this.tonnage]
            }
            get motiveType() {
                return super.motiveType
            }
            set motiveType(e) {
                if (e !== this._motiveType) {
                    const a = this._motiveType;
                    super.motiveType = e,
                    this.resetArmor(a),
                    this.resetLocations()
                }
            }
            get destinyMove() {
                return (this.walkMP > 0 ? this.walkMP + (this.runMP > 0 ? " / " + this.runMP : "") : "") + (this.jumpMP && this.jumpMP > 0 ? (this.walkMP > 0 ? " / " : "") + this.jumpMP + "j" : "") + (this.isEquipedWith("umu") ? (this.walkMP > 0 ? " / " : "") + this.walkMP + "u" : "")
            }
            get destinyTMM() {
                const e = this.tmm(this.walkMP)
                  , a = this.tmm(this.runMP)
                  , t = this.tmm(this.jumpMP) + 1;
                return (this.walkMP > 0 ? e + (this.runMP > 0 ? " / " + a : "") : "") + (this.jumpMP > 0 ? (this.walkMP > 0 ? " / " : "") + t : "") + (this.isEquipedWith("umu") ? (e > 0 ? " / " : "") + e : "")
            }
            get destinyWeapons() {
                var e = super.destinyWeapons;
                if (this.tonnage > 0) {
                    const a = {
                        melee: !0,
                        name: "Punch / Kick",
                        damage: this.isBlank ? "" : Math.ceil(Number(this.fixedTonnage) / 30) + " / " + Math.ceil(Number(this.fixedTonnage) / 15),
                        heat: "--",
                        location: "--",
                        rangePB: "+0",
                        rangeS: "--",
                        rangeM: "--",
                        rangeL: "--",
                        rangeX: "--"
                    };
                    e[9] = a
                }
                return e
            }
            validate() {
                var e = super.validate();
                return this._validate_mech(e),
                e
            }
            get motiveTypes() {
                return M.MotiveTypeEnum
            }
            get destinyLocations() {
                return this._motiveType === M.MotiveTypeEnum.BP ? Object.keys(M.BPDestinyLocationEnum).map(e => M.BPDestinyLocationEnum[e]) : this._motiveType === M.MotiveTypeEnum.QD ? Object.keys(M.QuadDestinyLocations).map(e => M.QuadDestinyLocations[e]) : []
            }
            get destinySinks() {
                var e = this.hasDHS ? 2 * this.sinks : this.sinks
                  , a = Math.round(Number(e || 0) / 5) + (this.isEquipedWith("partwing") ? 1 : 0);
                if (this.isEquipedWith("cpod")) {
                    var t = this.getEquipment("cpod");
                    +t.uses > 0 && (a += Math.round(this.sinks * t.uses / 10 / 5) + 1)
                }
                return this.isEquipedWith("stealth") && (a -= 2) < 0 && (a = 0),
                a
            }
            clone() {
                return new M(this)
            }
            destinyArmorValue(e) {
                var a = 0
                  , t = 3;
                return this._motiveType === M.MotiveTypeEnum.BP ? e === M.BPDestinyLocationEnum.T ? (a = this.armor.CT + this.armor.RT + this.armor.LT,
                t = 6) : e === M.BPDestinyLocationEnum.TR ? (a = this.armor.CTR + this.armor.LTR + this.armor.RTR,
                t = 6) : e === M.BPDestinyLocationEnum.HD ? (a = this.armor.HD <= 2 ? 1 : this.armor.HD <= 5 ? 2 : this.armor.HD <= 7 ? 3 : 4,
                t = 1) : a = +this.armor[e] : this._motiveType === M.MotiveTypeEnum.QD && (e === M.QuadDestinyLocations.T ? (a = this.armor.CT + this.armor.RT + this.armor.LT,
                t = 6) : e === M.QuadDestinyLocations.TR ? (a = this.armor.CTR + this.armor.LTR + this.armor.RTR,
                t = 6) : e === M.QuadDestinyLocations.HD ? (a = this.armor.HD <= 2 ? 1 : this.armor.HD <= 5 ? 2 : this.armor.HD <= 7 ? 3 : 4,
                t = 1) : a = +this.armor[e]),
                Math.max(Math.round(a / t), 1)
            }
            destinyStructureValue(e) {
                var a = 0
                  , t = 3;
                this._motiveType === M.MotiveTypeEnum.BP ? e === M.BPDestinyLocationEnum.HD ? a = this.structure.HD : e === M.BPDestinyLocationEnum.T ? (a = this.structure.CT + 2 * this.structure.ST,
                t = 7) : [M.BPDestinyLocationEnum.LA, M.BPDestinyLocationEnum.RA].includes(e) ? a = this.structure.AR : [M.BPDestinyLocationEnum.LL, M.BPDestinyLocationEnum.RL].includes(e) && (a = this.structure.LG) : this._motiveType === M.MotiveTypeEnum.QD && (e === M.QuadDestinyLocations.HD ? a = this.structure.HD : e === M.QuadDestinyLocations.T ? (a = this.structure.CT + 2 * this.structure.ST,
                t = 7) : [M.QuadDestinyLocations.LFL, M.QuadDestinyLocations.RFL, M.QuadDestinyLocations.LRL, M.QuadDestinyLocations.RRL].includes(e) && (a = this.structure.LG));
                var n = Math.max(Math.round(a / t), 1);
                return this.isEquipedWith("composite") && (n = Math.max(Math.round(n / 2), 1)),
                n
            }
            weaponArc(e) {
                return [M.BPLocationEnum.T, M.BPLocationEnum.LL, M.BPLocationEnum.RL, M.BPLocationEnum.HD, M.QDLocationEnum.T, M.QDLocationEnum.LFL, M.QDLocationEnum.RFL, M.QDLocationEnum.LRL, M.QDLocationEnum.RRL, M.QDLocationEnum.HD].includes(e) ? A.WeaponArcEnum.Front : [M.BPLocationEnum.RT, M.BPLocationEnum.RLL, M.BPLocationEnum.RRL, M.BPLocationEnum.RHD, M.QDLocationEnum.RLFL, M.QDLocationEnum.RRFL, M.QDLocationEnum.RLRL, M.QDLocationEnum.RRRL, M.QDLocationEnum.RT, M.QDLocationEnum.RHD].includes(e) ? A.WeaponArcEnum.Rear : A.WeaponArcEnum.Any
            }
            _validate_mech(e) {
                this.sinks < 0 && (e.sinks = "Heat Dissipation cannot be less than 0."),
                this.walk < 0 && (e.walk = "Walk MP cannot be less than 0."),
                this.jump < 0 && (e.jump = "Jump MP cannot be less than 0."),
                this.armor.HD < 0 ? e.armorHD = "Armor cannot be less than 0." : this.armor.HD > 9 && (e.armorHD = "Armor maximum is 9 for this unit, mass and location."),
                this.armor.LT < 0 ? e.armorLT = "Armor cannot be less than 0." : Number(this.armor.LT) + Number(this.armor.LTR) > 2 * this.structure.ST && (e.armorLT = "Armor maximum is " + 2 * this.structure.ST + " for this unit, mass and locations (front + rear)."),
                this.armor.LTR < 0 ? e.armorLTR = "Armor cannot be less than 0." : Number(this.armor.LTR) + Number(this.armor.LT) > 2 * this.structure.ST && (e.armorLTR = "Armor maximum is " + 2 * this.structure.ST + " for this unit, mass and locations (front + rear)."),
                this.armor.CT < 0 ? e.armorCT = "Armor cannot be less than 0." : Number(this.armor.CT) + Number(this.armor.CTR) > 2 * this.structure.CT && (e.armorCT = "Armor maximum is " + 2 * this.structure.CT + " for this unit, mass and locations (front + rear)."),
                this.armor.CTR < 0 ? e.armorCTR = "Armor cannot be less than 0." : Number(this.armor.CTR) + Number(this.armor.CT) > 2 * this.structure.CT && (e.armorCTR = "Armor maximum is " + 2 * this.structure.CT + " for this unit, mass and locations (front + rear)."),
                this.armor.RT < 0 ? e.armorRT = "Armor cannot be less than 0." : Number(this.armor.RT) + Number(this.armor.RTR) > 2 * this.structure.ST && (e.armorRT = "Armor maximum is " + 2 * this.structure.ST + " for this unit, mass and locations (front + rear)."),
                this.armor.RTR < 0 ? e.armorRTR = "Armor cannot be less than 0." : Number(this.armor.RTR) + Number(this.armor.RT) > 2 * this.structure.ST && (e.armorRTR = "Armor maximum is " + 2 * this.structure.ST + " for this unit, mass and locations (front + rear)."),
                this.motiveType === M.MotiveTypeEnum.BP ? (this.armor.LA < 0 ? e.armorLA = "Armor cannot be less than 0." : this.armor.LA > 2 * this.structure.AR && (e.armorLA = "Armor maximum is " + 2 * this.structure.AR + " for this unit, mass and location."),
                this.armor.RA < 0 ? e.armorRA = "Armor cannot be less than 0." : this.armor.RA > 2 * this.structure.AR && (e.armorRA = "Armor maximum is " + 2 * this.structure.AR + " for this unit, mass and location."),
                this.armor.LL < 0 ? e.armorLL = "Armor cannot be less than 0." : this.armor.LL > 2 * this.structure.LG && (e.armorLL = "Armor maximum is " + 2 * this.structure.LG + " for this unit, mass and location."),
                this.armor.RL < 0 ? e.armorRL = "Armor cannot be less than 0." : this.armor.RL > 2 * this.structure.LG && (e.armorRL = "Armor maximum is " + 2 * this.structure.LG + " for this unit, mass and location.")) : this.motiveType === M.MotiveTypeEnum.QD && (this.armor.LFL < 0 ? e.armorLFL = "Armor cannot be less than 0." : this.armor.LFL > 2 * this.structure.LG && (e.armorLFL = "Armor maximum is " + 2 * this.structure.LG + " for this unit, mass and location."),
                this.armor.RFL < 0 ? e.armorRFL = "Armor cannot be less than 0." : this.armor.RFL > 2 * this.structure.LG && (e.armorRFL = "Armor maximum is " + 2 * this.structure.LG + " for this unit, mass and location."),
                this.armor.LRL < 0 ? e.armorLRL = "Armor cannot be less than 0." : this.armor.LRL > 2 * this.structure.LG && (e.armorLRL = "Armor maximum is " + 2 * this.structure.LG + " for this unit, mass and location."),
                this.armor.RRL < 0 ? e.armorRRL = "Armor cannot be less than 0." : this.armor.RRL > 2 * this.structure.LG && (e.armorRRL = "Armor maximum is " + 2 * this.structure.LG + " for this unit, mass and location."))
            }
        }
        M.BPLocationEnum = Object.seal({
            T: "T",
            LA: "LA",
            RA: "RA",
            LL: "LL",
            RL: "RL",
            HD: "HD",
            RT: "(R) T",
            RLL: "(R) LL",
            RRL: "(R) RL",
            RHD: "(R) HD"
        }),
        M.QDLocationEnum = Object.seal({
            T: "T",
            LFL: "LFL",
            RFL: "RFL",
            LRL: "LRL",
            RRL: "RRL",
            HD: "HD",
            TU: "TU",
            RT: "(R) T",
            RLFL: "(R) LFL",
            RRFL: "(R) RFL",
            RLRL: "(R) LRL",
            RRRL: "(R) RRL",
            RHD: "(R) HD"
        }),
        M.BPArmorEnum = Object.seal({
            HD: "HD",
            LA: "LA",
            RA: "RA",
            LT: "LT",
            CT: "CT",
            RT: "RT",
            LL: "LL",
            RL: "RL",
            LTR: "LTR",
            CTR: "CTR",
            RTR: "RTR"
        }),
        M.QDArmorEnum = Object.seal({
            HD: "HD",
            LT: "LT",
            CT: "CT",
            RT: "RT",
            LFL: "LFL",
            RFL: "RFL",
            LRL: "LRL",
            RRL: "RRL",
            LTR: "LTR",
            CTR: "CTR",
            RTR: "RTR"
        }),
        M.BPDestinyLocationEnum = Object.seal({
            HD: "HD",
            LA: "LA",
            RA: "RA",
            T: "T",
            LL: "LL",
            RL: "RL",
            TR: "TR"
        }),
        M.QuadDestinyLocations = Object.seal({
            HD: "HD",
            T: "T",
            LFL: "LFL",
            RFL: "RFL",
            LRL: "LRL",
            RRL: "RRL",
            TR: "TR"
        }),
        M.MotiveTypeEnum = Object.seal({
            BP: "Biped",
            QD: "Quad"
        }),
        M.STRUCTURE_DATA = {
            20: {
                HD: 3,
                CT: 6,
                ST: 5,
                AR: 3,
                LG: 4,
                A2: 69,
                A4: 73
            },
            25: {
                HD: 3,
                CT: 8,
                ST: 6,
                AR: 4,
                LG: 6,
                A2: 89,
                A4: 97
            },
            30: {
                HD: 3,
                CT: 10,
                ST: 7,
                AR: 5,
                LG: 7,
                A2: 105,
                A4: 113
            },
            35: {
                HD: 3,
                CT: 11,
                ST: 8,
                AR: 6,
                LG: 8,
                A2: 119,
                A4: 127
            },
            40: {
                HD: 3,
                CT: 12,
                ST: 10,
                AR: 6,
                LG: 10,
                A2: 137,
                A4: 153
            },
            45: {
                HD: 3,
                CT: 14,
                ST: 11,
                AR: 7,
                LG: 11,
                A2: 153,
                A4: 169
            },
            50: {
                HD: 3,
                CT: 16,
                ST: 12,
                AR: 8,
                LG: 12,
                A2: 169,
                A4: 185
            },
            55: {
                HD: 3,
                CT: 18,
                ST: 13,
                AR: 9,
                LG: 13,
                A2: 185,
                A4: 201
            },
            60: {
                HD: 3,
                CT: 20,
                ST: 14,
                AR: 10,
                LG: 14,
                A2: 201,
                A4: 217
            },
            65: {
                HD: 3,
                CT: 21,
                ST: 15,
                AR: 10,
                LG: 15,
                A2: 211,
                A4: 231
            },
            70: {
                HD: 3,
                CT: 22,
                ST: 15,
                AR: 11,
                LG: 15,
                A2: 217,
                A4: 233
            },
            75: {
                HD: 3,
                CT: 23,
                ST: 16,
                AR: 12,
                LG: 16,
                A2: 231,
                A4: 247
            },
            80: {
                HD: 3,
                CT: 25,
                ST: 17,
                AR: 13,
                LG: 17,
                A2: 247,
                A4: 263
            },
            85: {
                HD: 3,
                CT: 27,
                ST: 18,
                AR: 14,
                LG: 18,
                A2: 263,
                A4: 279
            },
            90: {
                HD: 3,
                CT: 29,
                ST: 19,
                AR: 15,
                LG: 19,
                A2: 279,
                A4: 295
            },
            95: {
                HD: 3,
                CT: 30,
                ST: 20,
                AR: 16,
                LG: 20,
                A2: 293,
                A4: 309
            },
            100: {
                HD: 3,
                CT: 31,
                ST: 21,
                AR: 17,
                LG: 21,
                A2: 307,
                A4: 323
            }
        };
        const L = M;
        var f = t(1093)
          , S = t(6430)
          , b = t(4414);
        class C extends n.Component {
            constructor() {
                super(...arguments),
                this.getDestiny = () => null != localStorage.getItem("destiny") && localStorage.getItem("destiny").includes('"isDestinyEnabled":true'),
                this.getDestinyInverse = () => 1 != this.getDestiny()
            }
            render() {
                const e = this.props.unit
                  , a = e.locations
                  , t = e.weapons
                  , n = e.tech
                  , s = this.props.onAdd
                  , l = this.props.onRemove
                  , o = this.props.onChange
                  , m = this.props.errors
                  , u = g.Data
                  , h = x.GroupNumbers;
                return (0,
                b.jsxs)(c.A.Body, {
                    className: "p-0 pt-2",
                    children: [(0,
                    b.jsx)("h6", {
                        children: e.type === A.UnitTypeEnum.BA ? "'Mech-Scale Weapons (per suit)" : "Weapons"
                    }), (0,
                    b.jsx)("div", {
                        className: m.weapons ? "d-block invalid-feedback" : "d-none",
                        children: m.weapons
                    }), (0,
                    b.jsx)("div", {
                        className: m.weapons ? "border border-danger" : "",
                        children: (0,
                        b.jsxs)(f.A, {
                            responsive: !0,
                            striped: !0,
                            hover: !0,
                            className: "text-left datafont w-max",
                            variant: "dark",
                            size: "sm",
                            children: [(0,
                            b.jsx)("thead", {
                                children: (0,
                                b.jsxs)("tr", {
                                    children: [(0,
                                    b.jsxs)("th", {
                                        children: ["+/-", (0,
                                        b.jsx)("span", {
                                            className: "pr-3"
                                        })]
                                    }), (0,
                                    b.jsx)("th", {
                                        className: "text-center",
                                        style: {
                                            minWidth: "55px"
                                        },
                                        children: "TIC"
                                    }), (0,
                                    b.jsx)("th", {
                                        className: "text-center",
                                        children: "Weapon"
                                    }), (0,
                                    b.jsx)("th", {
                                        className: "text-center",
                                        children: "Loc"
                                    }), (0,
                                    b.jsx)("th", {
                                        className: "text-center",
                                        children: "Ammo"
                                    })]
                                })
                            }), (0,
                            b.jsxs)("tbody", {
                                children: [t.map( (t, s) => {
                                    let m = new x;
                                    m.weapons.push(t);
                                    let c = y.groupData(m);
                                    c.damage,
                                    c.heat,
                                    c.rangePB,
                                    c.rangeS,
                                    c.rangeM,
                                    c.rangeL,
                                    c.rangeX;
                                    return (0,
                                    b.jsxs)("tr", {
                                        children: [(0,
                                        b.jsxs)("td", {
                                            children: [(0,
                                            b.jsx)(i.A, {
                                                value: s,
                                                "data-item": "weapons",
                                                onClick: l,
                                                disabled: e.isBlank,
                                                variant: "secondary",
                                                size: "sm",
                                                children: (0,
                                                b.jsx)(S.zKP, {})
                                            }), (0,
                                            b.jsx)("span", {
                                                className: "pr-3"
                                            })]
                                        }), (0,
                                        b.jsx)("td", {
                                            children: (0,
                                            b.jsx)(r.A.Control, {
                                                as: "select",
                                                value: t.tic,
                                                "data-item": "weapons",
                                                "data-index": s,
                                                "data-property": "tic",
                                                onChange: o,
                                                disabled: e.isBlank || e.type === A.UnitTypeEnum.BA,
                                                size: "sm",
                                                custom: !0,
                                                children: h.map(e => (0,
                                                b.jsx)("option", {
                                                    children: e
                                                }, e))
                                            })
                                        }), (0,
                                        b.jsxs)("td", {
                                            className: "d-none d-md-table-cell",
                                            children: [1 == this.getDestiny() && (0,
                                            b.jsxs)(r.A.Control, {
                                                as: "select",
                                                value: t.id,
                                                "data-item": "weapons",
                                                "data-index": s,
                                                "data-property": "id",
                                                onChange: o,
                                                disabled: e.isBlank,
                                                isInvalid: !t.id,
                                                size: "sm",
                                                custom: !0,
                                                children: [(0,
                                                b.jsx)("option", {
                                                    disabled: !0
                                                }), Object.keys(u).map(e => {
                                                    const a = A.TechEnum[u[e].tech];
                                                    return "Mixed" === n || "Mixed" === a || n === a || t.id === e ? (0,
                                                    b.jsx)("option", {
                                                        value: e,
                                                        children: u[e].fullname
                                                    }, e) : ""
                                                }
                                                )]
                                            }), 0 == this.getDestiny() && (0,
                                            b.jsxs)(r.A.Control, {
                                                as: "select",
                                                value: t.id,
                                                "data-item": "weapons",
                                                "data-index": s,
                                                "data-property": "id",
                                                onChange: o,
                                                disabled: e.isBlank,
                                                isInvalid: !t.id,
                                                size: "sm",
                                                custom: !0,
                                                children: [(0,
                                                b.jsx)("option", {
                                                    disabled: !0
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "mg",
                                                    children: "MG"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ac2",
                                                    children: "Autocannon/2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ac5",
                                                    children: "Autocannon/5"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ac10",
                                                    children: "Autocannon/10"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ac20",
                                                    children: "Autocannon/20"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "srm2",
                                                    children: "SRM-2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "srm4",
                                                    children: "SRM-4"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "srm6",
                                                    children: "SRM-6"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "lrm5",
                                                    children: "LRM-5"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "lrm10",
                                                    children: "LRM-10"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "lrm15",
                                                    children: "LRM-15"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "lrm20",
                                                    children: "LRM-20"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "flamer",
                                                    children: "Flamer"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "slas",
                                                    children: "Small Laser"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "mlas",
                                                    children: "Medium Laser"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "llas",
                                                    children: "Large Laser"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ppc",
                                                    children: "PPC"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cmg",
                                                    children: "cMG"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clb2x",
                                                    children: "Clan LB 2-X Autocannon"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clb5x",
                                                    children: "Clan LB 5-X Autocannon"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clb10x",
                                                    children: "Clan LB 10-X Autocannon"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clb20x",
                                                    children: "Clan LB 20-X Autocannon"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cuac2",
                                                    children: "Clan Ultra Autocannon/2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cuac5",
                                                    children: "Clan Ultra Autocannon/5"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cuac10",
                                                    children: "Clan Ultra Autocannon/10"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cuac20",
                                                    children: "Clan Ultra Autocannon/20"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cgauss",
                                                    children: "Clan Gauss Rifle"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "csrm2",
                                                    children: "Clan SRM-2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "csrm4",
                                                    children: "Clan SRM-4"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "csrm6",
                                                    children: "Clan SRM-6"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cssrm2",
                                                    children: "Clan Streak SRM-2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cssrm4",
                                                    children: "Clan Streak SRM-4"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cssrm6",
                                                    children: "Clan Streak SRM-6"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clrm5",
                                                    children: "Clan LRM-5"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clrm10",
                                                    children: "Clan LRM-10"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clrm15",
                                                    children: "Clan LRM-15"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clrm20",
                                                    children: "Clan LRM-20"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cerslas",
                                                    children: "Clan ER Small Laser"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cermlas",
                                                    children: "Clan ER Medium Laser"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cerllas",
                                                    children: "Clan ER Large Laser"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "csplas",
                                                    children: "Clan Small Pulse Laser"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cmplas",
                                                    children: "Clan Medium Pulse Laser"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clplas",
                                                    children: "Clan Large Pulse Laser"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cerppc",
                                                    children: "Clan ER PPC"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cflamer",
                                                    children: "cFlamer"
                                                })]
                                            })]
                                        }), (0,
                                        b.jsxs)("td", {
                                            className: "d-md-none",
                                            children: [1 == this.getDestiny() && (0,
                                            b.jsxs)(r.A.Control, {
                                                as: "select",
                                                value: t.id,
                                                "data-item": "weapons",
                                                "data-index": s,
                                                "data-property": "id",
                                                onChange: o,
                                                disabled: e.isBlank,
                                                isInvalid: !t.id,
                                                size: "sm",
                                                custom: !0,
                                                children: [(0,
                                                b.jsx)("option", {
                                                    disabled: !0
                                                }), Object.keys(u).map(e => {
                                                    const a = A.TechEnum[u[e].tech];
                                                    return "Mixed" === n || "Mixed" === a || n === a || t.id === e ? (0,
                                                    b.jsx)("option", {
                                                        value: e,
                                                        children: u[e].name
                                                    }, e) : ""
                                                }
                                                )]
                                            }), 0 == this.getDestiny() && (0,
                                            b.jsxs)(r.A.Control, {
                                                as: "select",
                                                value: t.id,
                                                "data-item": "weapons",
                                                "data-index": s,
                                                "data-property": "id",
                                                onChange: o,
                                                disabled: e.isBlank,
                                                isInvalid: !t.id,
                                                size: "sm",
                                                custom: !0,
                                                children: [(0,
                                                b.jsx)("option", {
                                                    disabled: !0
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "mg",
                                                    children: "MG"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ac2",
                                                    children: "AC/2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ac5",
                                                    children: "AC/5"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ac10",
                                                    children: "AC/10"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ac20",
                                                    children: "AC/20"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "srm2",
                                                    children: "SRM-2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "srm4",
                                                    children: "SRM-4"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "srm6",
                                                    children: "SRM-6"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "lrm5",
                                                    children: "LRM-5"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "lrm10",
                                                    children: "LRM-10"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "lrm15",
                                                    children: "LRM-15"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "lrm20",
                                                    children: "LRM-20"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "flamer",
                                                    children: "Flamer"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "slas",
                                                    children: "SLas"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "mlas",
                                                    children: "MLas"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "llas",
                                                    children: "LLas"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "ppc",
                                                    children: "PPC"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cmg",
                                                    children: "cMG"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clb2x",
                                                    children: "cLB 2-X"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clb5x",
                                                    children: "cLB 5-X"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clb10x",
                                                    children: "cLB 10-X"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clb20x",
                                                    children: "cLB 20-X"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cuac2",
                                                    children: "cUAC/2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cuac5",
                                                    children: "cUAC/5"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cuac10",
                                                    children: "cUAC/10"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cuac20",
                                                    children: "cUAC/20"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cgauss",
                                                    children: "cGauss"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "csrm2",
                                                    children: "cSRM-2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "csrm4",
                                                    children: "cSRM-4"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "csrm6",
                                                    children: "cSRM-6"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cssrm2",
                                                    children: "cSSRM-2"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cssrm4",
                                                    children: "cSSRM-4"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cssrm6",
                                                    children: "cSSRM-6"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clrm5",
                                                    children: "cLRM-5"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clrm10",
                                                    children: "cLRM-10"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clrm15",
                                                    children: "cLRM-15"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clrm20",
                                                    children: "cLRM-20"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cerslas",
                                                    children: "cerSLas"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cermlas",
                                                    children: "cerMLas"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cerllas",
                                                    children: "cerLLas"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "csplas",
                                                    children: "cSPLas"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cmplas",
                                                    children: "cMPLas"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "clplas",
                                                    children: "cLPLas"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cerppc",
                                                    children: "cerPPC"
                                                }), (0,
                                                b.jsx)("option", {
                                                    value: "cflamer",
                                                    children: "cFlamer"
                                                })]
                                            })]
                                        }), (0,
                                        b.jsx)("td", {
                                            children: (0,
                                            b.jsxs)(r.A.Control, {
                                                as: "select",
                                                value: t.location,
                                                "data-item": "weapons",
                                                "data-index": s,
                                                "data-property": "location",
                                                onChange: o,
                                                disabled: e.isBlank,
                                                isInvalid: !t.location,
                                                size: "sm",
                                                custom: !0,
                                                children: [(0,
                                                b.jsx)("option", {
                                                    disabled: !0
                                                }), a && a.map(e => (0,
                                                b.jsx)("option", {
                                                    children: e
                                                }, e))]
                                            })
                                        }), (0,
                                        b.jsx)("td", {
                                            children: t.hasAmmoOption ? (0,
                                            b.jsx)(r.A.Control, {
                                                as: "select",
                                                value: t.ammo,
                                                "data-item": "weapons",
                                                "data-index": s,
                                                "data-property": "ammo",
                                                onChange: o,
                                                disabled: e.isBlank,
                                                size: "sm",
                                                custom: !0,
                                                children: Object.values(y.AmmoTypeEnum).map(e => (0,
                                                b.jsx)("option", {
                                                    value: e,
                                                    children: e
                                                }, e))
                                            }) : null
                                        })]
                                    }, s)
                                }
                                ), t.length <= 20 && (0,
                                b.jsxs)("tr", {
                                    children: [(0,
                                    b.jsxs)("td", {
                                        children: [(0,
                                        b.jsx)(i.A, {
                                            "data-item": "weapons",
                                            disabled: "" === n || e.isBlank,
                                            onClick: s,
                                            size: "sm",
                                            children: (0,
                                            b.jsx)(S.ivV, {})
                                        }), (0,
                                        b.jsx)("span", {
                                            className: "pr-3"
                                        })]
                                    }), (0,
                                    b.jsx)("td", {
                                        colSpan: "10"
                                    })]
                                })]
                            })]
                        })
                    })]
                })
            }
        }
        const T = C;
        class R extends n.Component {
            constructor() {
                super(...arguments),
                this.getDestiny = () => null != localStorage.getItem("destiny") && localStorage.getItem("destiny").includes('"isDestinyEnabled":true'),
                this.getDestinyInverse = () => 1 != this.getDestiny()
            }
            render() {
                const e = this.props.unit
                  , a = e.locations
                  , t = e.equipment
                  , n = e.tech
                  , s = this.props.onAdd
                  , l = this.props.onRemove
                  , o = this.props.onChange
                  , m = this.props.errors
                  , u = h.Data;
                return (0,
                b.jsxs)(c.A.Body, {
                    className: "p-0 pt-2",
                    children: [(0,
                    b.jsx)("h6", {
                        children: "Equipment"
                    }), (0,
                    b.jsx)("div", {
                        className: m.equipment ? "d-block invalid-feedback" : "d-none",
                        children: m.equipment
                    }), (0,
                    b.jsx)("div", {
                        className: m.equipment ? "border border-danger" : "",
                        children: (0,
                        b.jsxs)(f.A, {
                            responsive: !0,
                            striped: !0,
                            hover: !0,
                            className: "text-left datafont w-max",
                            variant: "dark",
                            size: "sm",
                            children: [(0,
                            b.jsx)("thead", {
                                children: (0,
                                b.jsxs)("tr", {
                                    children: [(0,
                                    b.jsxs)("th", {
                                        children: ["+/-", (0,
                                        b.jsx)("span", {
                                            className: "pr-3"
                                        })]
                                    }), (0,
                                    b.jsx)("th", {
                                        className: "text-center",
                                        children: "Equipment"
                                    }), (0,
                                    b.jsx)("th", {
                                        className: "text-center",
                                        children: "Loc"
                                    }), (0,
                                    b.jsx)("th", {
                                        className: "text-center",
                                        children: "Subtype"
                                    }), (0,
                                    b.jsx)("th", {
                                        className: "text-center",
                                        children: "Uses"
                                    })]
                                })
                            }), (0,
                            b.jsxs)("tbody", {
                                children: [t.map( (t, s) => (0,
                                b.jsxs)("tr", {
                                    children: [(0,
                                    b.jsxs)("td", {
                                        children: [(0,
                                        b.jsx)(i.A, {
                                            value: s,
                                            "data-item": "equipment",
                                            onClick: l,
                                            disabled: e.isBlank,
                                            variant: "secondary",
                                            size: "sm",
                                            children: (0,
                                            b.jsx)(S.zKP, {})
                                        }), (0,
                                        b.jsx)("span", {
                                            className: "pr-3"
                                        })]
                                    }), (0,
                                    b.jsxs)("td", {
                                        className: "d-none d-md-table-cell",
                                        children: [1 == this.getDestiny() && (0,
                                        b.jsxs)(r.A.Control, {
                                            as: "select",
                                            value: t.id,
                                            "data-item": "equipment",
                                            "data-index": s,
                                            "data-property": "id",
                                            onChange: o,
                                            disabled: e.isBlank,
                                            isInvalid: !t.id,
                                            size: "sm",
                                            custom: !0,
                                            children: [(0,
                                            b.jsx)("option", {
                                                disabled: !0
                                            }), Object.keys(u).map(e => {
                                                const a = A.TechEnum[u[e].tech];
                                                return "Mixed" === n || "Mixed" === a || n === a ? (0,
                                                b.jsxs)("option", {
                                                    value: e,
                                                    children: ["Mixed" === n && "Clan" === a && "(c)", u[e].fullname]
                                                }, e) : ""
                                            }
                                            )]
                                        }), 0 == this.getDestiny() && (0,
                                        b.jsxs)(r.A.Control, {
                                            as: "select",
                                            value: t.id,
                                            "data-item": "equipment",
                                            "data-index": s,
                                            "data-property": "id",
                                            onChange: o,
                                            disabled: e.isBlank,
                                            isInvalid: !t.id,
                                            size: "sm",
                                            custom: !0,
                                            children: [(0,
                                            b.jsx)("option", {
                                                disabled: !0
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "ammo",
                                                children: "Ammo"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "cprobe",
                                                children: "Active Probe"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "apod",
                                                children: "A-Pods"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "ams",
                                                children: "Anti-Missile System"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "freecase",
                                                children: "Built-in CASE"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "masc",
                                                children: "MASC"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "tc",
                                                children: "Targeting Computer"
                                            })]
                                        })]
                                    }), (0,
                                    b.jsxs)("td", {
                                        className: "d-md-none",
                                        children: [1 == this.getDestiny() && (0,
                                        b.jsxs)(r.A.Control, {
                                            as: "select",
                                            value: t.id,
                                            "data-item": "equipment",
                                            "data-index": s,
                                            "data-property": "id",
                                            onChange: o,
                                            disabled: e.isBlank,
                                            isInvalid: !t.id,
                                            size: "sm",
                                            custom: !0,
                                            children: [(0,
                                            b.jsx)("option", {
                                                disabled: !0
                                            }), Object.keys(u).map(e => {
                                                const a = A.TechEnum[u[e].tech];
                                                return "Mixed" === n || "Mixed" === a || n === a ? (0,
                                                b.jsxs)("option", {
                                                    value: e,
                                                    children: ["Mixed" === n && "Clan" === a && "(c)", u[e].name]
                                                }, e) : ""
                                            }
                                            )]
                                        }), 0 == this.getDestiny() && (0,
                                        b.jsxs)(r.A.Control, {
                                            as: "select",
                                            value: t.id,
                                            "data-item": "equipment",
                                            "data-index": s,
                                            "data-property": "id",
                                            onChange: o,
                                            disabled: e.isBlank,
                                            isInvalid: !t.id,
                                            size: "sm",
                                            custom: !0,
                                            children: [(0,
                                            b.jsx)("option", {
                                                disabled: !0
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "ammo",
                                                children: "Ammo"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "cprobe",
                                                children: "Active Probe"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "apod",
                                                children: "A-Pods"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "ams",
                                                children: "AMS"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "freecase",
                                                children: "CASE"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "masc",
                                                children: "MASC"
                                            }), (0,
                                            b.jsx)("option", {
                                                value: "tc",
                                                children: "Targeting Computer"
                                            })]
                                        })]
                                    }), (0,
                                    b.jsx)("td", {
                                        children: t.hasLoc ? (0,
                                        b.jsxs)(r.A.Control, {
                                            as: "select",
                                            value: t.location,
                                            "data-item": "equipment",
                                            "data-index": s,
                                            "data-property": "location",
                                            onChange: o,
                                            disabled: e.isBlank,
                                            isInvalid: !t.location,
                                            size: "sm",
                                            custom: !0,
                                            children: [(0,
                                            b.jsx)("option", {
                                                disabled: !0
                                            }), a && a.map(e => (0,
                                            b.jsx)("option", {
                                                children: e
                                            }, e))]
                                        }) : null
                                    }), (0,
                                    b.jsx)("td", {
                                        children: t.subtypes ? (0,
                                        b.jsxs)(r.A.Control, {
                                            as: "select",
                                            value: t.subtype,
                                            "data-item": "equipment",
                                            "data-index": s,
                                            "data-property": "subtype",
                                            onChange: o,
                                            disabled: e.isBlank,
                                            isInvalid: !t.subtype,
                                            size: "sm",
                                            custom: !0,
                                            children: [(0,
                                            b.jsx)("option", {
                                                disabled: !0
                                            }), t.subtypes && Object.keys(t.subtypes).map(e => (0,
                                            b.jsx)("option", {
                                                value: e,
                                                children: t.subtypes[e]
                                            }, e))]
                                        }) : null
                                    }), (0,
                                    b.jsx)("td", {
                                        children: t.isLimited ? (0,
                                        b.jsx)(r.A.Control, {
                                            type: "number",
                                            value: t.uses,
                                            "data-item": "equipment",
                                            "data-index": s,
                                            "data-property": "uses",
                                            onChange: o,
                                            disabled: e.isBlank,
                                            isInvalid: !t.id,
                                            size: "sm"
                                        }) : null
                                    }), t.subtypes || t.isLimited ? null : (0,
                                    b.jsx)("td", {})]
                                }, s)), t.length <= 20 && (0,
                                b.jsxs)("tr", {
                                    children: [(0,
                                    b.jsxs)("td", {
                                        children: [(0,
                                        b.jsx)(i.A, {
                                            "data-item": "equipment",
                                            disabled: "" === n || e.isBlank,
                                            onClick: s,
                                            size: "sm",
                                            children: (0,
                                            b.jsx)(S.ivV, {})
                                        }), (0,
                                        b.jsx)("span", {
                                            className: "pr-3"
                                        })]
                                    }), (0,
                                    b.jsx)("td", {
                                        colSpan: "10"
                                    })]
                                })]
                            })]
                        })
                    })]
                })
            }
        }
        const j = R;
        class w extends n.Component {
            constructor() {
                super(...arguments),
                this.getDestiny = () => null != localStorage.getItem("destiny") && localStorage.getItem("destiny").includes('"isDestinyEnabled":true'),
                this.getDestinyInverse = () => 1 != this.getDestiny()
            }
            render() {
                return (0,
                b.jsxs)(c.A, {
                    className: "p-0",
                    children: [(0,
                    b.jsx)(c.A.Header, {
                        children: (0,
                        b.jsx)("div", {
                            className: "d-flex",
                            children: (0,
                            b.jsx)("span", {
                                className: "ml-auto",
                                children: (0,
                                b.jsxs)(b.Fragment, {
                                    children: [(0,
                                    b.jsx)(i.A, {
                                        onClick: this.props.onSort,
                                        className: "mr-3",
                                        size: "sm",
                                        disabled: this.getDestinyInverse(),
                                        children: "Sort"
                                    }), (0,
                                    b.jsx)(i.A, {
                                        onClick: this.props.onGroup,
                                        className: "mr-3",
                                        size: "sm",
                                        disabled: this.getDestinyInverse(),
                                        children: "Auto-Group"
                                    }), (0,
                                    b.jsx)(i.A, {
                                        onClick: this.props.onClear,
                                        size: "sm",
                                        children: "Clear"
                                    })]
                                })
                            })
                        })
                    }), (0,
                    b.jsxs)(c.A.Body, {
                        children: [(0,
                        b.jsx)(T, {
                            unit: this.props.unit,
                            onAdd: this.props.onAdd,
                            onRemove: this.props.onRemove,
                            onChange: this.props.onChange,
                            errors: this.props.errors
                        }), (0,
                        b.jsx)("hr", {
                            className: "m-0 mb-2"
                        }), (0,
                        b.jsx)(j, {
                            unit: this.props.unit,
                            onAdd: this.props.onAdd,
                            onRemove: this.props.onRemove,
                            onChange: this.props.onChange,
                            errors: this.props.errors
                        })]
                    })]
                })
            }
        }
        const E = w;
        class B extends n.Component {
            render() {
                return this.props.unit.motiveType === L.MotiveTypeEnum.BP ? (0,
                b.jsx)(P, {
                    unit: this.props.unit,
                    onChange: this.props.onChange,
                    errors: this.props.errors
                }) : this.props.unit.motiveType === L.MotiveTypeEnum.QD ? (0,
                b.jsx)(k, {
                    unit: this.props.unit,
                    onChange: this.props.onChange,
                    errors: this.props.errors
                }) : void 0
            }
        }
        const P = e => {
            let {unit: a, onChange: t, errors: n} = e;
            return (0,
            b.jsx)(c.A, {
                className: "pt-2",
                children: (0,
                b.jsxs)(c.A.Body, {
                    children: [(0,
                    b.jsxs)(r.A.Row, {
                        className: "justify-content-center",
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.LA",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Left Arm"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.LA,
                                isInvalid: !!n.armorLA,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorLA
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.HD",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Head"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.HD,
                                isInvalid: !!n.armorHD,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorHD
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.RA",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Right Arm"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.RA,
                                isInvalid: !!n.armorRA,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorRA
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        className: "justify-content-center",
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.LT",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Left Torso"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.LT,
                                isInvalid: !!n.armorLT,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorLT
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.CT",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Center Torso"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.CT,
                                isInvalid: !!n.armorCT,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorCT
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.RT",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Right Torso"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.RT,
                                isInvalid: !!n.armorRT,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorRT
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        className: "justify-content-center",
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.LTR",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Left Torso Rear"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.LTR,
                                isInvalid: !!n.armorLTR,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorLTR
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.CTR",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Center Torso Rear"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.CTR,
                                isInvalid: !!n.armorCTR,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorCTR
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.RTR",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Right Torso Rear"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.RTR,
                                isInvalid: !!n.armorRTR,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorRTR
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        className: "justify-content-center",
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.LL",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Left Leg"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.LL,
                                isInvalid: !!n.armorLL,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorLL
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.RL",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Right Leg"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.RL,
                                isInvalid: !!n.armorRL,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorRL
                            })]
                        })]
                    })]
                })
            })
        }
          , k = e => {
            let {unit: a, onChange: t, errors: n} = e;
            return (0,
            b.jsx)(c.A, {
                className: "pt-2",
                children: (0,
                b.jsxs)(c.A.Body, {
                    children: [(0,
                    b.jsxs)(r.A.Row, {
                        className: "justify-content-center",
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.LFL",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Left Front Leg"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.LFL,
                                isInvalid: !!n.armorLFL,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorLFL
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.HD",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Head"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.HD,
                                isInvalid: !!n.armorHD,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorHD
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.RFL",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Right Front Leg"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.RFL,
                                isInvalid: !!n.armorRFL,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorRFL
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        className: "justify-content-center",
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.LT",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Left Torso"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.LT,
                                isInvalid: !!n.armorLT,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorLT
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.CT",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Center Torso"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.CT,
                                isInvalid: !!n.armorCT,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorCT
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.RT",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Right Torso"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.RT,
                                isInvalid: !!n.armorRT,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorRT
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        className: "justify-content-center",
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.LTR",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Left Torso Rear"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.LTR,
                                isInvalid: !!n.armorLTR,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorLTR
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.CTR",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Center Torso Rear"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.CTR,
                                isInvalid: !!n.armorCTR,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorCTR
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.RTR",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Right Torso Rear"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.RTR,
                                isInvalid: !!n.armorRTR,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorRTR
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        className: "justify-content-center",
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.LRL",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Left Rear Leg"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.LRL,
                                isInvalid: !!n.armorLRL,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorLRL
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.RRL",
                            xs: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Right Rear Leg"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: a.armor.RRL,
                                isInvalid: !!n.armorRRL,
                                onChange: t,
                                disabled: a.isBlank,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: n.armorRRL
                            })]
                        })]
                    })]
                })
            })
        }
          , I = B;
        class F extends n.Component {
            constructor() {
                super(...arguments),
                this.getDestiny = () => null != localStorage.getItem("destiny") && localStorage.getItem("destiny").includes('"isDestinyEnabled":true')
            }
            render() {
                const e = this.props.unit
                  , a = this.props.onChange
                  , t = this.props.onAddItem
                  , n = this.props.onRemoveItem
                  , i = this.props.onChangeItem
                  , m = this.props.onSortItems
                  , c = this.props.onGroupWeapons
                  , u = this.props.onClearItems
                  , h = this.props.errors;
                return (0,
                b.jsxs)(b.Fragment, {
                    children: [(0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "chassis",
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Chassis"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "text",
                                value: e.chassis,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "variant",
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: e.isOmni ? "Config" : "Variant"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "text",
                                value: e.variant,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "tonnage",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Tonnage"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.tonnage,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedTonnage.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "tech",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Tech"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.tech,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), Object.keys(L.TechEnum).map(e => (0,
                                b.jsx)("option", {
                                    value: L.TechEnum[e],
                                    children: L.TechEnum[e]
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "isOmni",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {}), (0,
                            b.jsx)(r.A.Check, {
                                label: "Omni-tech",
                                type: "checkbox",
                                value: e.isOmni,
                                disabled: e.isBlank,
                                checked: e.isOmni,
                                onChange: a,
                                className: "ml-3",
                                custom: !0
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "walk",
                            xs: 6,
                            sm: 3,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Walk MP"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: e.walk,
                                isInvalid: !!h.walk,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: h.walk
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "jump",
                            xs: 6,
                            sm: 3,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Jump MP"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: e.jump,
                                isInvalid: !!h.jump,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: h.jump
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Heat Sinks"
                            }), (0,
                            b.jsxs)(r.A.Row, {
                                children: [(0,
                                b.jsx)(r.A.Group, {
                                    controlId: "sinks",
                                    as: s.A,
                                    children: (0,
                                    b.jsx)(r.A.Control, {
                                        type: "number",
                                        value: e.sinks,
                                        isInvalid: !!h.sinks,
                                        disabled: e.isBlank,
                                        onChange: a,
                                        size: "sm"
                                    })
                                }), (0,
                                b.jsx)(r.A.Group, {
                                    controlId: "hasDHS",
                                    as: s.A,
                                    children: (0,
                                    b.jsx)(r.A.Check, {
                                        label: "Double",
                                        type: "checkbox",
                                        value: e.hasDHS,
                                        checked: e.hasDHS,
                                        disabled: e.isBlank,
                                        onChange: a,
                                        className: "ml-3",
                                        custom: !0
                                    })
                                })]
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: h.sinks
                            })]
                        })]
                    }), (0,
                    b.jsx)(r.A.Row, {
                        children: (0,
                        b.jsx)(r.A.Group, {
                            as: s.A,
                            controlId: "showOmittedEquipment",
                            xs: 12,
                            sm: 6,
                            children: (0,
                            b.jsx)(r.A.Check, {
                                label: "Show Omitted Equipment",
                                type: "checkbox",
                                value: e.showOmittedEquipment,
                                checked: e.showOmittedEquipment,
                                disabled: e.isBlank,
                                onChange: a,
                                className: "ml-3",
                                custom: !0
                            })
                        })
                    }), (0,
                    b.jsx)(r.A.Row, {
                        children: (0,
                        b.jsx)(s.A, {
                            xs: 12,
                            children: (0,
                            b.jsxs)(l.A, {
                                defaultActiveKey: "loadout",
                                id: "unitTabs",
                                className: "h6 m-0 mt-3",
                                transition: !1,
                                children: [(0,
                                b.jsx)(o.A, {
                                    eventKey: "loadout",
                                    title: "Loadout",
                                    children: (0,
                                    b.jsx)(E, {
                                        unit: e,
                                        onAdd: t,
                                        onRemove: n,
                                        onChange: i,
                                        onSort: m,
                                        onGroup: c,
                                        onClear: u,
                                        errors: h
                                    })
                                }), (0,
                                b.jsx)(o.A, {
                                    eventKey: "armor",
                                    title: "Armor",
                                    children: (0,
                                    b.jsx)(I, {
                                        unit: e,
                                        onChange: a,
                                        errors: h
                                    })
                                })]
                            })
                        })
                    })]
                })
            }
        }
        const q = F;
        class X extends A {
            constructor(e) {
                var a;
                (super(e),
                this._cruise = 0,
                this.type = A.UnitTypeEnum.CV,
                e instanceof X) ? (this._chassis = e.chassis,
                this._clanname = e.clanname,
                this._variant = e.variant,
                this._motiveType = e.motiveType,
                this._hasTurret = e.hasTurret,
                this._tonnage = e.tonnage,
                this._tech = e.tech,
                this._omni = e.isOmni,
                this._cruise = e.cruise,
                this._armor = e.armor,
                this._weapons = [],
                null === (a = e.weapons) || void 0 === a || a.forEach(e => {
                    this.addWeapon(new y(this,e))
                }
                ),
                this._equipment = e.equipment,
                this._showOmittedEquipment = e.showOmittedEquipment) : (this._hasTurret = !1,
                this._motiveType = X.MotiveTypeEnum.T,
                this._tonnage = this.allowedTonnage[0],
                this.resetArmor());
                this.resetLocations()
            }
            get cruise() {
                return this._cruise
            }
            set cruise(e) {
                !isNaN(+e) && +e >= 0 && (this._cruise = +e)
            }
            get hasTurret() {
                return this._hasTurret
            }
            set hasTurret(e) {
                this._hasTurret !== !!e && (this._hasTurret = !!e,
                this._hasTurret ? this._armor[X.LocationsEnum.TU] = 1 : (delete this._armor[X.LocationsEnum.TU],
                this.resetLocations()))
            }
            get cruiseMP() {
                var e = Number(this.cruise) || 0;
                return e > 0 && this.isEquipedWith("supercharger") && (e = Math.ceil(1.25 * e)),
                e
            }
            get flankMP() {
                return Math.max(Math.round(1.5 * this.cruiseMP) + (this.isEquipedWith("hardened") ? -1 : 0), 0)
            }
            resetArmor() {
                const e = this._armor;
                this._armor = {},
                this.destinyLocations.forEach(a => {
                    this._armor[a] = e[a] || 1
                }
                ),
                delete this._armor[X.LocationsEnum.BD]
            }
            resetLocations() {
                this.locations = this.destinyLocations
            }
            get supportedImports() {
                return [A.ImportTypeEnum.MML]
            }
            get locations() {
                let e = super.locations.slice();
                return this.motiveType === X.MotiveTypeEnum.V && e.indexOf(X.LocationsEnum.RO) >= 0 && e.splice(e.indexOf(X.LocationsEnum.RO), 1),
                e
            }
            set locations(e) {
                super.locations = e
            }
            get motiveType() {
                return super.motiveType
            }
            set motiveType(e) {
                e !== this._motiveType && (super.motiveType = e,
                this.motiveType === X.MotiveTypeEnum.V && (this.hasTurret = !1),
                this.resetArmor())
            }
            get structure() {
                let e = Math.ceil(this.tonnage / 10)
                  , a = {};
                return Object.values(X.LocationsEnum).forEach(t => {
                    t !== X.LocationsEnum.BD && (a[t] = e)
                }
                ),
                a
            }
            get allowedTonnage() {
                switch (this.motiveType) {
                case X.MotiveTypeEnum.V:
                    return [5, 10, 15, 20, 25, 30];
                case X.MotiveTypeEnum.H:
                    return [5, 10, 15, 20, 25, 30, 35, 40, 45, 50];
                case X.MotiveTypeEnum.W:
                    return [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80];
                default:
                    return [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
                }
            }
            get typeName() {
                return this.isOmni ? "Omni-Vehicle" : "Combat Vehicle"
            }
            get destinyMove() {
                return this.cruiseMP > 0 ? this.cruiseMP + (this.flankMP > 0 ? " / " + this.flankMP : "") + this.motiveType.charAt(0).toLowerCase() : ""
            }
            get destinyTMM() {
                const e = this.tmm(this.cruiseMP)
                  , a = this.tmm(this.flankMP);
                return this.cruiseMP > 0 ? e + (this.flankMP > 0 ? " / " + a : "") : ""
            }
            tmm(e) {
                return super.tmm(e) + (this.motiveType === X.MotiveTypeEnum.V ? 1 : 0)
            }
            validate() {
                var e = super.validate();
                return this._validate_cv(e),
                e
            }
            get motiveTypes() {
                return X.MotiveTypeEnum
            }
            get destinyLocations() {
                let e = Object.assign({}, X.LocationsEnum);
                return this.hasTurret && this.motiveType !== X.MotiveTypeEnum.V || delete e[X.LocationsEnum.TU],
                this.motiveType !== X.MotiveTypeEnum.V && delete e[X.LocationsEnum.RO],
                Object.values(e)
            }
            clone() {
                return new X(this)
            }
            destinyArmorValue(e) {
                return Object.keys(X.LocationsEnum).includes(e) ? Math.max(Math.round(this.armor[e] / 4), 1) : 0
            }
            destinyStructureValue(e) {
                return Math.max(Math.round(Math.ceil(this.tonnage / 10) / 3), 1)
            }
            weaponArc(e) {
                return e === X.LocationsEnum.FR ? A.WeaponArcEnum.Front : e === X.LocationsEnum.RR ? A.WeaponArcEnum.Rear : e === X.LocationsEnum.LS ? A.WeaponArcEnum.Left : e === X.LocationsEnum.RS ? A.WeaponArcEnum.Right : A.WeaponArcEnum.Any
            }
            _validate_cv(e) {
                this.cruise < 0 && (e.cruise = "Cruise MP cannot be less than 0."),
                this.allowedTonnage.includes(this.tonnage) || (e.tonnage = "Invalid tonnage for motive type '" + this.motiveType + "'.");
                let a = 0
                  , t = Math.floor(3.5 * this.tonnage + 40);
                Object.keys(this.armor).forEach(e => {
                    e !== X.LocationsEnum.BD && (a += this.armor[e])
                }
                ),
                a > t && (e.armor = "Total armor cannot exceed " + t + "."),
                this.motiveType === X.MotiveTypeEnum.V && (this.armor.RO || 0) > 2 && (e.armorRO = "Rotors cannot have more than 2 armor.")
            }
        }
        X.MotiveTypeEnum = Object.seal({
            T: "Tracked",
            W: "Wheeled",
            H: "Hover",
            V: "VTOL"
        }),
        X.LocationsEnum = Object.seal({
            BD: "BD",
            FR: "FR",
            LS: "LS",
            RS: "RS",
            RR: "RR",
            TU: "TU",
            RO: "RO"
        });
        class N extends n.Component {
            render() {
                const e = this.props.unit
                  , a = this.props.onChange
                  , t = this.props.errors;
                return (0,
                b.jsx)(c.A, {
                    className: "pt-2",
                    children: (0,
                    b.jsxs)(c.A.Body, {
                        children: [(0,
                        b.jsxs)(r.A.Row, {
                            className: "justify-content-center",
                            children: [(0,
                            b.jsx)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.LS",
                                xs: 4,
                                children: (0,
                                b.jsx)(r.A.Label, {})
                            }), (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.FR",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Front"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[X.LocationsEnum.FR],
                                    isInvalid: !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            }), (0,
                            b.jsx)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.RS",
                                xs: 4,
                                children: (0,
                                b.jsx)(r.A.Label, {})
                            })]
                        }), (0,
                        b.jsxs)(r.A.Row, {
                            className: "justify-content-center",
                            children: [(0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.LS",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Left Side"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[X.LocationsEnum.LS],
                                    isInvalid: !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            }), e.hasTurret ? (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.TU",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Turret"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[X.LocationsEnum.TU],
                                    isInvalid: !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            }) : null, e.motiveType === X.MotiveTypeEnum.V ? (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.RO",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Rotor"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[X.LocationsEnum.RO],
                                    isInvalid: !!t.armorRO || !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armorRO
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            }) : null, (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.RS",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Right Side"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[X.LocationsEnum.RS],
                                    isInvalid: !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            })]
                        }), (0,
                        b.jsx)(r.A.Row, {
                            className: "justify-content-center",
                            children: (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.RR",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Rear"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[X.LocationsEnum.RR],
                                    isInvalid: !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            })
                        })]
                    })
                })
            }
        }
        const W = N;
        class z extends n.Component {
            constructor() {
                super(...arguments),
                this.getDestiny = () => null != localStorage.getItem("destiny") && localStorage.getItem("destiny").includes('"isDestinyEnabled":true')
            }
            render() {
                const e = this.props.unit
                  , a = this.props.onChange
                  , t = this.props.onAddItem
                  , n = this.props.onRemoveItem
                  , i = this.props.onChangeItem
                  , m = this.props.onSortItems
                  , c = this.props.onGroupWeapons
                  , u = this.props.onClearItems
                  , h = this.props.errors;
                return (0,
                b.jsxs)(b.Fragment, {
                    children: [(0,
                    b.jsx)(r.A.Row, {
                        children: e.motiveType !== X.MotiveTypeEnum.V ? (0,
                        b.jsx)(r.A.Group, {
                            as: s.A,
                            controlId: "hasTurret",
                            xs: 12,
                            sm: 6,
                            children: (0,
                            b.jsx)(r.A.Check, {
                                label: "Has Turret",
                                type: "checkbox",
                                value: e.hasTurret,
                                checked: e.hasTurret,
                                onChange: a,
                                className: "ml-3",
                                custom: !0
                            })
                        }) : null
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "chassis",
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Chassis"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "text",
                                value: e.chassis,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "variant",
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: e.isOmni ? "Config" : "Variant"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "text",
                                value: e.variant,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "tonnage",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Tonnage"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.tonnage,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedTonnage.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "tech",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Tech"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.tech,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), Object.keys(X.TechEnum).map(e => (0,
                                b.jsx)("option", {
                                    value: X.TechEnum[e],
                                    children: X.TechEnum[e]
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "isOmni",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {}), (0,
                            b.jsx)(r.A.Check, {
                                label: "Omni-tech",
                                type: "checkbox",
                                value: e.isOmni,
                                disabled: e.isBlank,
                                checked: e.isOmni,
                                onChange: a,
                                className: "ml-3",
                                custom: !0
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "cruise",
                            xs: 6,
                            sm: 3,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Cruise MP"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: e.cruise,
                                isInvalid: !!h.cruise,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: h.cruise
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "showOmittedEquipment",
                            xs: 6,
                            sm: 3,
                            children: [(0,
                            b.jsx)(r.A.Label, {}), (0,
                            b.jsx)(r.A.Check, {
                                label: "Show Omitted Equipment",
                                type: "checkbox",
                                value: e.showOmittedEquipment,
                                checked: e.showOmittedEquipment,
                                disabled: e.isBlank,
                                onChange: a,
                                className: "ml-3",
                                custom: !0
                            })]
                        })]
                    }), (0,
                    b.jsx)(r.A.Row, {
                        children: (0,
                        b.jsx)(s.A, {
                            xs: 12,
                            children: (0,
                            b.jsxs)(l.A, {
                                defaultActiveKey: "loadout",
                                id: "unitTabs",
                                className: "h6 m-0 mt-3",
                                transition: !1,
                                children: [(0,
                                b.jsx)(o.A, {
                                    eventKey: "loadout",
                                    title: "Loadout",
                                    children: (0,
                                    b.jsx)(E, {
                                        unit: e,
                                        onAdd: t,
                                        onRemove: n,
                                        onChange: i,
                                        onSort: m,
                                        onGroup: c,
                                        onClear: u,
                                        errors: h
                                    })
                                }), (0,
                                b.jsx)(o.A, {
                                    eventKey: "armor",
                                    title: "Armor",
                                    children: (0,
                                    b.jsx)(W, {
                                        unit: e,
                                        onChange: a,
                                        errors: h
                                    })
                                })]
                            })
                        })
                    })]
                })
            }
        }
        const G = z;
        class O extends A {
            constructor(e) {
                var a;
                (super(e),
                this.type = A.UnitTypeEnum.BA,
                e instanceof O) ? (this._chassis = e.chassis,
                this._clanname = e.clanname,
                this._variant = e.variant,
                this._motiveType = e.motiveType,
                this._weightClass = e.weightClass,
                this._tech = e.tech,
                this._squadSize = e.squadSize,
                this._groundMP = e.groundMP,
                this._otherMotiveType = e.otherMotiveType,
                this._otherMP = e.otherMP,
                this._armor = e.armor,
                this._weapons = [],
                null === (a = e.weapons) || void 0 === a || a.forEach(e => {
                    this.addWeapon(new y(this,e))
                }
                ),
                this._equipment = e.equipment,
                this._showOmittedEquipment = e.showOmittedEquipment) : (this._motiveType = O.MotiveTypeEnum.Biped,
                this._weightClass = O.WeightClassEnum.Medium,
                this._tech = A.TechEnum.Clan,
                this._squadSize = this.allowedSquadSize[0],
                this.resetMotives(),
                this.resetArmor());
                this.resetLocations()
            }
            get allowedWeightClasses() {
                const e = Object.keys(O.WeightClassEnum);
                return this.motiveType === O.MotiveTypeEnum.Quad ? e.slice(1) : e
            }
            get weightClass() {
                return this._weightClass
            }
            set weightClass(e) {
                e && Object.values(O.WeightClassEnum).includes(e) && (this._weightClass = e,
                this.resetMotives(),
                this.resetArmor())
            }
            get allowedSquadSize() {
                return this.isBlank ? [4, 5, 6] : this.tech === A.TechEnum.Clan ? [5] : [4, 5, 6]
            }
            get squadSize() {
                return this._squadSize
            }
            set squadSize(e) {
                e && this.allowedSquadSize.includes(+e) && (this._squadSize = +e)
            }
            get allowedGroundMP() {
                for (var e = [], a = this.minGroundMP; a <= this.maxGroundMP; a++)
                    e.push(a);
                return e
            }
            get groundMP() {
                return this._groundMP
            }
            set groundMP(e) {
                !isNaN(+e) && +e >= 0 && (this._groundMP = +e)
            }
            get allowedOtherMP() {
                for (var e = [], a = 0; a <= this.maxOtherMP; a++)
                    e.push(a);
                return e
            }
            get otherMP() {
                return this._otherMP
            }
            set otherMP(e) {
                !isNaN(+e) && +e >= 0 && (this._otherMP = +e)
            }
            get allowedOtherMotiveTypes() {
                return this.motiveType === O.MotiveTypeEnum.Biped ? this.tech === A.TechEnum.IS ? [O.OtherMotiveTypeEnum.None, O.OtherMotiveTypeEnum.Jump] : [O.WeightClassEnum.Heavy, O.WeightClassEnum.Assault].includes(this.weightClass) ? [O.OtherMotiveTypeEnum.None, O.OtherMotiveTypeEnum.Jump, O.OtherMotiveTypeEnum.UMU] : Object.values(O.OtherMotiveTypeEnum) : [O.OtherMotiveTypeEnum.None]
            }
            get otherMotiveType() {
                return this._otherMotiveType
            }
            set otherMotiveType(e) {
                e && Object.values(O.OtherMotiveTypeEnum).includes(e) && (this._otherMotiveType = e),
                this.otherMotiveType === O.OtherMotiveTypeEnum.None && (this.otherMP = 0)
            }
            get walkMP() {
                var e = this.groundMP;
                return this.isEquipedWith("myomerboost") && ([O.WeightClassEnum.Heavy, O.WeightClassEnum.Assault].includes(this.weightClass) ? e += 1 : e += 2),
                e
            }
            get runMP() {
                return Math.max(Math.round(1.5 * this.walkMP), 0)
            }
            get jumpMP() {
                var e = this.otherMP;
                return this.otherMotiveType === O.OtherMotiveTypeEnum.Jump && (this.isEquipedWith("partwing") || this.isEquipedWith("jumpbooster")) && (e += 1),
                e
            }
            get minGroundMP() {
                return this.motiveType === O.MotiveTypeEnum.Biped ? 1 : 2
            }
            get maxGroundMP() {
                if (this.motiveType === O.MotiveTypeEnum.Biped)
                    switch (this.weightClass) {
                    case O.WeightClassEnum.PAL:
                    case O.WeightClassEnum.Light:
                    case O.WeightClassEnum.Medium:
                        return 3;
                    case O.WeightClassEnum.Heavy:
                    case O.WeightClassEnum.Assault:
                        return 2;
                    default:
                        return 0
                    }
                else
                    switch (this.weightClass) {
                    case O.WeightClassEnum.Light:
                    case O.WeightClassEnum.Medium:
                        return 5;
                    case O.WeightClassEnum.Heavy:
                    case O.WeightClassEnum.Assault:
                        return 4;
                    default:
                        return 0
                    }
            }
            get maxOtherMP() {
                if (this.motiveType === O.MotiveTypeEnum.Biped)
                    switch (this.weightClass) {
                    case O.WeightClassEnum.PAL:
                        switch (this.otherMotiveType) {
                        case O.OtherMotiveTypeEnum.Jump:
                            return 3;
                        case O.OtherMotiveTypeEnum.VTOL:
                            return 7;
                        case O.OtherMotiveTypeEnum.UMU:
                            return 5;
                        default:
                            return 0
                        }
                    case O.WeightClassEnum.Light:
                        switch (this.otherMotiveType) {
                        case O.OtherMotiveTypeEnum.Jump:
                            return 3;
                        case O.OtherMotiveTypeEnum.VTOL:
                            return 6;
                        case O.OtherMotiveTypeEnum.UMU:
                            return 5;
                        default:
                            return 0
                        }
                    case O.WeightClassEnum.Medium:
                        switch (this.otherMotiveType) {
                        case O.OtherMotiveTypeEnum.Jump:
                            return 3;
                        case O.OtherMotiveTypeEnum.VTOL:
                            return 5;
                        case O.OtherMotiveTypeEnum.UMU:
                            return 4;
                        default:
                            return 0
                        }
                    case O.WeightClassEnum.Heavy:
                        switch (this.otherMotiveType) {
                        case O.OtherMotiveTypeEnum.Jump:
                            return 2;
                        case O.OtherMotiveTypeEnum.VTOL:
                            return 0;
                        case O.OtherMotiveTypeEnum.UMU:
                            return 3;
                        default:
                            return 0
                        }
                    case O.WeightClassEnum.Assault:
                        switch (this.otherMotiveType) {
                        case O.OtherMotiveTypeEnum.Jump:
                            return 2;
                        case O.OtherMotiveTypeEnum.VTOL:
                            return 0;
                        case O.OtherMotiveTypeEnum.UMU:
                            return 2;
                        default:
                            return 0
                        }
                    default:
                        return 0
                    }
                return 0
            }
            get allowedArmor() {
                var e, a = [];
                switch (this.weightClass) {
                case O.WeightClassEnum.PAL:
                    e = 2;
                    break;
                case O.WeightClassEnum.Light:
                    e = 6;
                    break;
                case O.WeightClassEnum.Medium:
                    e = 10;
                    break;
                case O.WeightClassEnum.Heavy:
                    e = 14;
                    break;
                case O.WeightClassEnum.Assault:
                    e = 18;
                    break;
                default:
                    e = 0
                }
                for (var t = 0; t <= e; t++)
                    a.push(t);
                return a
            }
            get weaponLimits() {
                return this.motiveType === O.MotiveTypeEnum.Biped ? {
                    [O.LocationsEnum.Arm]: 2,
                    [O.LocationsEnum.Body]: 2
                } : {
                    [O.LocationsEnum.Arm]: 0,
                    [O.LocationsEnum.Body]: 4
                }
            }
            get hasAntiMech() {
                return this.motiveType === O.MotiveTypeEnum.Biped && ![O.WeightClassEnum.Heavy, O.WeightClassEnum.Assault].includes(this.weightClass)
            }
            get hasMechanized() {
                return this.motiveType === O.MotiveTypeEnum.Biped && this.weightClass !== O.WeightClassEnum.Assault
            }
            resetMotives() {
                this.allowedGroundMP.includes(this.groundMP) || (this.groundMP = this.allowedGroundMP[0]),
                this.allowedOtherMotiveTypes.includes(this.otherMotiveType) || (this.otherMotiveType = O.OtherMotiveTypeEnum.None),
                this.allowedOtherMP.includes(this.otherMP) || (this.otherMP = this.allowedOtherMP[0])
            }
            resetArmor() {
                var e;
                null !== (e = this.armor) && void 0 !== e && e.Body && this.allowedArmor.includes(this.armor.Body) || (this.armor = {
                    Body: this.allowedArmor[this.allowedArmor.length - 1]
                })
            }
            resetLocations() {
                let e = Object.assign({}, O.LocationsEnum);
                this.isEquipedWith("turret") || delete e[O.LocationsEnum.TU],
                this.isEquipedWith("dwp") || delete e[O.LocationsEnum.DWP],
                this.motiveType !== O.MotiveTypeEnum.Biped && delete e[O.LocationsEnum.Arm],
                this.locations = Object.values(e)
            }
            get supportedImports() {
                return [A.ImportTypeEnum.MML]
            }
            get motiveType() {
                return super.motiveType
            }
            set motiveType(e) {
                e !== this._motiveType && (super.motiveType = e,
                this.otherMotiveType = O.OtherMotiveTypeEnum.None,
                this.allowedWeightClasses.includes(this.weightClass) || (this.weightClass = this.allowedWeightClasses[0]),
                this.resetMotives(),
                this.resetLocations())
            }
            get destinyMove() {
                return (this.walkMP > 0 ? this.walkMP + (this.runMP > 0 ? " / " + this.runMP : "") : "") + (this.jumpMP > 0 ? (this.jumpMP > 0 ? " / " : "") + this.jumpMP + ( () => {
                    switch (this.otherMotiveType) {
                    case O.OtherMotiveTypeEnum.Jump:
                        return "j";
                    case O.OtherMotiveTypeEnum.VTOL:
                        return "v";
                    case O.OtherMotiveTypeEnum.UMU:
                        return "u";
                    default:
                        return ""
                    }
                }
                )() : "")
            }
            get destinyTMM() {
                const e = this.tmm(this.walkMP)
                  , a = this.tmm(this.runMP)
                  , t = this.tmm(this.jumpMP) + (this.otherMotiveType === O.OtherMotiveTypeEnum.UMU ? 0 : 1);
                return (this.walkMP > 0 ? e + (this.runMP > 0 ? " / " + a : "") : "") + (this.jumpMP > 0 ? (this.walkMP > 0 ? " / " : "") + t : "")
            }
            tmm(e) {
                return super.tmm(e) + 1
            }
            get destinyEquipment() {
                var e = ""
                  , a = 0;
                return this.equipment.forEach(t => {
                    if (t.id && (!t.omit || this.showOmittedEquipment)) {
                        var n = a > 0 ? ", " : "";
                        n += t.name + (t.subtype ? ":" + t.subtype : "") + (t.uses && t.uses > 0 ? " [" + t.uses + ("ammolimited" === t.id ? " shots" : "") + "]" : ""),
                        e += n,
                        a++
                    }
                }
                ),
                e
            }
            get destinyWeapons() {
                const e = this.clone();
                e.sortWeapons();
                const a = e.tics;
                var t = new Array(5);
                for (let r = 0; r < a.length && r < 4; r++) {
                    let e = y.groupData(a[r]);
                    if (e.name) {
                        t[r] = e;
                        let s = [];
                        for (let e = this.squadSize; e > 0; e--) {
                            let t = new x;
                            for (let s = 1; s <= e; s++) {
                                var n;
                                null === (n = a[r]) || void 0 === n || n.weapons.forEach(e => {
                                    t.weapons.push(new y(this,e))
                                }
                                )
                            }
                            let i = y.groupData(t);
                            s.push(i.damage)
                        }
                        t[r].damage = s
                    }
                }
                const s = {
                    melee: !0,
                    name: "Anti-Infantry",
                    damage: this.isBlank ? "" : ( () => {
                        var e = [];
                        for (let a = this.squadSize; a > 0; a--)
                            e.push(a + "d6");
                        return e
                    }
                    )(),
                    heat: "--",
                    location: "--",
                    rangePB: "+0",
                    rangeS: "+0",
                    rangeM: "--",
                    rangeL: "--",
                    rangeX: "--"
                };
                return t[4] = s,
                t
            }
            get tech() {
                return super.tech
            }
            set tech(e) {
                e !== this._tech && (super.tech = e,
                this.resetMotives())
            }
            get tonnage() {
                const e = e => {
                    switch (e) {
                    case O.WeightClassEnum.PAL:
                        return .4;
                    case O.WeightClassEnum.Light:
                        return .75;
                    case O.WeightClassEnum.Medium:
                        return 1;
                    case O.WeightClassEnum.Heavy:
                        return 1.5;
                    case O.WeightClassEnum.Assault:
                        return 2;
                    default:
                        return 0
                    }
                }
                ;
                return Math.round(2 * e(this.weightClass)) / 2 + " ea. (" + Math.round(e(this.weightClass) * this.squadSize * 2) / 2 + " total)"
            }
            set tonnage(e) {}
            get typeName() {
                return this.type + (this.motiveType === O.MotiveTypeEnum.Quad ? " (Quad)" : "")
            }
            validate() {
                var e = super.validate();
                return this._validate_ba(e),
                e
            }
            get motiveTypes() {
                return O.MotiveTypeEnum
            }
            get destinyLocations() {
                return [O.LocationsEnum.Body]
            }
            clone() {
                return new O(this)
            }
            destinyArmorValue(e) {
                const a = this.armor && this.armor[e] || 0;
                return Math.max(Math.ceil(a / 4), 1)
            }
            destinyStructureValue(e) {
                return 1
            }
            weaponArc(e) {
                return A.WeaponArcEnum.Any
            }
            _validate_ba(e) {
                var a, t, n = 0, s = 0, r = (null === (a = this.weaponLimits) || void 0 === a ? void 0 : a[O.LocationsEnum.Body]) || 0, i = (null === (t = this.weaponLimits) || void 0 === t ? void 0 : t[O.LocationsEnum.Arm]) || 0;
                this.weapons.forEach(e => {
                    e.location === O.LocationsEnum.Body ? n++ : e.location === O.LocationsEnum.Arm && s++
                }
                ),
                n > r && (e.weapons || (e.weapons = "Errors: "),
                e.weapons += "This chassis/motive type only allows " + r + " Body slot(s) for 'Mech-Scale weaponry."),
                s > i && (e.weapons || (e.weapons = "Errors: "),
                e.weapons += "This chassis/motive type only allows " + i + " Arm slot(s) for 'Mech-Scale weaponry.")
            }
        }
        O.WeightClassEnum = Object.seal({
            PAL: "PA(L) / Exoskeleton",
            Light: "Light",
            Medium: "Medium",
            Heavy: "Heavy",
            Assault: "Assault"
        }),
        O.MotiveTypeEnum = Object.seal({
            Biped: "Biped",
            Quad: "Quad"
        }),
        O.OtherMotiveTypeEnum = Object.seal({
            None: "--None--",
            Jump: "Jump Jets",
            VTOL: "VTOL",
            UMU: "UMU"
        }),
        O.LocationsEnum = Object.seal({
            Body: "Body",
            Arm: "Arm",
            TU: "TU",
            DWP: "DWP"
        });
        const D = O;
        class U extends n.Component {
            render() {
                const e = this.props.unit
                  , a = this.props.onChange
                  , t = this.props.onAddItem
                  , n = this.props.onRemoveItem
                  , i = this.props.onChangeItem
                  , m = this.props.onSortItems
                  , c = this.props.onGroupWeapons
                  , u = this.props.onClearItems
                  , h = this.props.errors;
                return (0,
                b.jsxs)(b.Fragment, {
                    children: [(0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "chassis",
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Chassis"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "text",
                                value: e.chassis,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "variant",
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Variant"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "text",
                                value: e.variant,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "weightClass",
                            xs: 12,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Weight Class"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.weightClass,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedWeightClasses.map(e => (0,
                                b.jsx)("option", {
                                    value: D.WeightClassEnum[e],
                                    children: D.WeightClassEnum[e]
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "tech",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Tech"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.tech,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), Object.keys(D.TechEnum).map(e => (0,
                                b.jsx)("option", {
                                    value: D.TechEnum[e],
                                    children: D.TechEnum[e]
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "squadSize",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Squad Size"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.squadSize,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedSquadSize.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "groundMP",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Ground MP"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.groundMP,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedGroundMP.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "otherMotiveType",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Other Motive Type"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.otherMotiveType,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedOtherMotiveTypes.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "otherMP",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Other MP"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.otherMP,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedOtherMP.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "armor.Body",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Armor Points"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.armor.Body,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedArmor.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "showOmittedEquipment",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {}), (0,
                            b.jsx)(r.A.Check, {
                                label: "Show Omitted Equipment",
                                type: "checkbox",
                                value: e.showOmittedEquipment,
                                checked: e.showOmittedEquipment,
                                disabled: e.isBlank,
                                onChange: a,
                                className: "ml-3",
                                custom: !0
                            })]
                        })]
                    }), (0,
                    b.jsx)(r.A.Row, {
                        children: (0,
                        b.jsx)(s.A, {
                            xs: 12,
                            children: (0,
                            b.jsx)(l.A, {
                                defaultActiveKey: "loadout",
                                id: "unitTabs",
                                className: "h6 m-0 mt-3",
                                transition: !1,
                                children: (0,
                                b.jsx)(o.A, {
                                    eventKey: "loadout",
                                    title: "Loadout",
                                    children: (0,
                                    b.jsx)(E, {
                                        unit: e,
                                        onAdd: t,
                                        onRemove: n,
                                        onChange: i,
                                        onSort: m,
                                        onGroup: c,
                                        onClear: u,
                                        errors: h
                                    })
                                })
                            })
                        })
                    })]
                })
            }
        }
        const H = U;
        class V extends A {
            constructor(e) {
                super(e),
                this._motiveType = "",
                this._squadSize = 0,
                this._squadCount = 0,
                this._weaponType = "",
                this.type = A.UnitTypeEnum.IN,
                e instanceof V ? (this._variant = e.variant,
                this._motiveType = e.motiveType,
                this._squadSize = e.squadSize,
                this._squadCount = e.squadCount,
                this._weaponType = e.weaponType) : (this._motiveType = V.MotiveTypeEnum.F,
                this._squadSize = this.allowedSquadSize[this.allowedSquadSize.length - 1],
                this._squadCount = this.allowedSquadCount[this.allowedSquadCount.length - 1],
                this._weaponType = Object.keys(V.WEAPON_DATA)[0])
            }
            get _motive() {
                return V.MOTIVE_DATA[this.motiveType] || {}
            }
            get _weapon() {
                return V.WEAPON_DATA[this.weaponType] || {}
            }
            get squadSize() {
                return this._squadSize
            }
            set squadSize(e) {
                e && this._squadSize !== +e && this.allowedSquadSize.includes(+e) && (this._squadSize = +e,
                this.allowedSquadCount.includes(this.squadCount) || (this.squadCount = this.allowedSquadCount[this.allowedSquadCount.length - 1]))
            }
            get allowedSquadSize() {
                return this._motive.allowedSquadSize
            }
            get msgSquadSize() {
                if (this.motiveType) {
                    return "Motive allows max squad size " + this.allowedSquadSize[this.allowedSquadSize.length - 1] + "."
                }
                return ""
            }
            get squadCount() {
                return this._squadCount
            }
            set squadCount(e) {
                e && this.allowedSquadCount.includes(+e) && (this._squadCount = +e)
            }
            get maxSquads() {
                return Math.min(this._motive.maxSquads, Math.floor(this._motive.maxTroops / this.squadSize))
            }
            get allowedSquadCount() {
                var e = [];
                const a = this.maxSquads + (this._weapon.reduceSquads ? -1 : 0);
                for (var t = 1; t <= a; t++)
                    e.push(t);
                return e
            }
            get msgSquadCount() {
                return this.motiveType ? "Motive allows max " + this.maxSquads + " squads or " + this._motive.maxTroops + " troops." : ""
            }
            get troopCount() {
                return this.squadSize * this.squadCount
            }
            get weaponType() {
                return this._weaponType
            }
            set weaponType(e) {
                e && this._weaponType !== e && Object.keys(V.WEAPON_DATA).includes(e) && (this._weaponType = e,
                this.allowedSquadCount.includes(this.squadCount) || (this.squadCount = this.allowedSquadCount[this.allowedSquadCount.length - 1]))
            }
            get msgWeaponType() {
                return this._weapon.reduceMove && this.motiveType !== V.MotiveTypeEnum.T ? "Weapon reduces move" + (this._weapon.reduceSquads ? " and max squads" : "") + " by 1." : ""
            }
            get walkMP() {
                var e = 0;
                return e = this._motiveType === V.MotiveTypeEnum.J ? 1 : Number(this._motive.movePoints),
                this._weapon.reduceMove && this.motiveType !== V.MotiveTypeEnum.T && (e = Math.max(e - 1, 0)),
                e
            }
            get runMP() {
                return Math.round(1.5 * this.walkMP) || 1
            }
            get jumpMP() {
                var e = 0;
                return this._motiveType === V.MotiveTypeEnum.J && (e = Number(this._motive.movePoints),
                this._weapon.reduceMove && (e = Math.max(e - 1, 0))),
                e
            }
            get hasAntiMech() {
                return [V.MotiveTypeEnum.F, V.MotiveTypeEnum.J, V.MotiveTypeEnum.M].includes(this.motiveType)
            }
            get hasMechanized() {
                return !1
            }
            weaponDamage(e) {
                var a = "";
                if (this.weaponType && e > 0 && e <= this.squadCount) {
                    var t;
                    if (null === (t = this._weapon) || void 0 === t || !t.damage)
                        return a;
                    const s = e * this.squadSize
                      , r = this._weapon.damage(s)
                      , i = Math.ceil(r / 3) || 0;
                    if (0 === i)
                        a = "0";
                    else {
                        if (this._weapon.useM) {
                            const e = Math.ceil(i / 2)
                              , t = Math.ceil((i - e) / 3);
                            a += e + (t > 0 ? "+M" + t + " (" + i + ")" : "")
                        } else {
                            const e = Math.floor(i / 2)
                              , t = i % 2;
                            for (var n = 1; n <= e; n++)
                                a += "2",
                                (n < e || t) && (a += ",");
                            t && (a += "1")
                        }
                        this._weapon.useH && (a += "+H" + Math.max(Math.round(r / 5), 1))
                    }
                }
                return a
            }
            get chassis() {
                var e;
                return (null === (e = this._motive.name) || void 0 === e ? void 0 : e.trim()) + " " || 0
            }
            set chassis(e) {}
            get typeName() {
                return this.variant ? this.chassis : "Conventional"
            }
            get motiveType() {
                return super.motiveType
            }
            set motiveType(e) {
                e !== this._motiveType && (super.motiveType = e,
                this.allowedSquadSize.includes(this.squadSize) || (this.squadSize = this.allowedSquadSize[this.allowedSquadSize.length - 1]),
                this.allowedSquadCount.includes(this.squadCount) || (this.squadCount = this.allowedSquadCount[this.allowedSquadCount.length - 1]))
            }
            get tonnage() {
                return Math.ceil(this._motive.baseWeight * this.troopCount) || ""
            }
            set tonnage(e) {}
            get cardName() {
                return (this.variant || this.chassis).toUpperCase()
            }
            get destinyMove() {
                return this.walkMP + (this.runMP > 0 ? " / " + this.runMP : "") + (this.jumpMP > 0 ? " / " + this.jumpMP + "j" : "") + (this._motive.moveType ? this._motive.moveType : "")
            }
            get destinyTMM() {
                const e = this.tmm(this.walkMP)
                  , a = this.tmm(this.runMP)
                  , t = this.tmm(this.jumpMP) + 1;
                return e + (this.runMP > 0 ? " / " + a : "") + (this.jumpMP > 0 ? " / " + t : "")
            }
            get destinyWeapons() {
                for (var e = [], a = [], t = this.squadCount; t > 0; t--)
                    a.push(this.weaponDamage(t) || "0");
                return e.push({
                    name: this._weapon.name + (this._weapon.antiinfantry ? " (AI)" : "") || "",
                    damage: a,
                    rangePB: this._weapon.rangePB || "--",
                    rangeS: this._weapon.rangeS || "--",
                    rangeM: this._weapon.rangeM || "--",
                    rangeL: this._weapon.rangeL || "--",
                    rangeX: this._weapon.rangeX || "--"
                }),
                e
            }
            get motiveTypes() {
                return V.MotiveTypeEnum
            }
            get destinyLocations() {
                return []
            }
            clone() {
                return new V(this)
            }
            destinyArmorValue(e) {
                return 0
            }
            destinyStructureValue(e) {
                return 0
            }
            weaponArc(e) {
                return A.WeaponArcEnum.Any
            }
        }
        V.MotiveTypeEnum = Object.seal({
            F: "Foot",
            M: "Motorized",
            J: "Jump",
            H: "Mechanized Hover",
            T: "Mechanized Tracked",
            W: "Mechanized Wheeled"
        }),
        V.MOTIVE_DATA = {
            Foot: {
                name: "Foot Infantry",
                allowedSquadSize: [5, 6, 7],
                isAllowedSize10: !0,
                maxSquads: 5,
                maxTroops: 30,
                movePoints: 1,
                baseWeight: .085
            },
            Motorized: {
                name: "Motorized Infantry",
                allowedSquadSize: [5, 6, 7],
                isAllowedSize10: !0,
                maxSquads: 5,
                maxTroops: 30,
                movePoints: 3,
                baseWeight: .195
            },
            Jump: {
                name: "Jump Infantry",
                allowedSquadSize: [5, 6, 7],
                isAllowedSize10: !0,
                maxSquads: 4,
                maxTroops: 24,
                movePoints: 3,
                baseWeight: .165
            },
            "Mechanized Hover": {
                name: "Mechanized Infantry (H)",
                allowedSquadSize: [4, 5],
                isAllowedSize10: !1,
                maxSquads: 4,
                maxTroops: 20,
                movePoints: 5,
                moveType: "h",
                baseWeight: 1
            },
            "Mechanized Tracked": {
                name: "Mechanized Infantry (T)",
                allowedSquadSize: [5, 6, 7],
                isAllowedSize10: !1,
                maxSquads: 4,
                maxTroops: 28,
                movePoints: 3,
                moveType: "t",
                baseWeight: 1
            },
            "Mechanized Wheeled": {
                name: "Mechanized Infantry (W)",
                allowedSquadSize: [5, 6],
                isAllowedSize10: !1,
                maxSquads: 4,
                maxTroops: 24,
                movePoints: 4,
                moveType: "w",
                baseWeight: 1
            }
        },
        V.WEAPON_DATA = {
            ballistic: {
                name: "Ballistic Rifle",
                damage: e => Math.round(e / 30 * 16),
                rangePB: "+0",
                rangeS: "+2",
                rangeM: "--"
            },
            laser: {
                name: "Laser Rifle",
                damage: e => Math.round(e / 30 * 8),
                rangePB: "+0",
                rangeS: "+2",
                rangeM: "+4"
            },
            mg: {
                name: "Machine Gun",
                damage: e => Math.round(e / 30 * 17),
                rangePB: "+0",
                rangeS: "+2",
                rangeM: "--",
                reduceMove: !0,
                antiinfantry: !0
            },
            flamer: {
                name: "Flamer",
                damage: e => Math.round(e / 30 * 14),
                rangePB: "+0",
                rangeS: "+2",
                rangeM: "--",
                useH: !0,
                reduceMove: !0,
                antiinfantry: !0
            },
            srm: {
                name: "SRM",
                damage: e => Math.round(e / 30 * 15),
                rangePB: "+0",
                rangeS: "+2",
                rangeM: "+4",
                useM: !0,
                reduceMove: !0
            },
            lrm: {
                name: "LRM",
                damage: e => Math.round(e / 30 * 13),
                rangePB: "+0",
                rangeS: "+0",
                rangeM: "+2",
                useM: !0,
                reduceMove: !0,
                reduceSquads: !0
            }
        };
        const J = V;
        class Q extends n.Component {
            render() {
                const e = this.props.unit
                  , a = this.props.onChange;
                return (0,
                b.jsxs)(b.Fragment, {
                    children: [(0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "squadSize",
                            xs: 6,
                            sm: 3,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Troops per Squad"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.squadSize,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedSquadSize.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            }), (0,
                            b.jsx)(r.A.Text, {
                                muted: !0,
                                children: e.msgSquadSize
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "squadCount",
                            xs: 6,
                            sm: 3,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Squads in Platoon"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.squadCount,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedSquadCount.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            }), (0,
                            b.jsx)(r.A.Text, {
                                muted: !0,
                                children: e.msgSquadCount
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "weaponType",
                            xs: 6,
                            sm: 3,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Weapon Type"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.weaponType,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), Object.keys(J.WEAPON_DATA).map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: J.WEAPON_DATA[e].name
                                }, e))]
                            }), (0,
                            b.jsx)(r.A.Text, {
                                muted: !0,
                                children: e.msgWeaponType
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "variant",
                            xs: 6,
                            sm: 3,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Unique Name"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "text",
                                value: e.variant,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            })]
                        })]
                    })]
                })
            }
        }
        const _ = Q;
        class K extends A {
            constructor(e) {
                var a;
                (super(e),
                this._sinks = {
                    count: 0,
                    isDHS: !1
                },
                this._thrust = 0,
                this._armor = {},
                this._tonnages = Object.seal([5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]),
                this._locations = Object.values(K.LocationEnum),
                this.type = A.UnitTypeEnum.AF,
                e instanceof K) ? (this._chassis = e.chassis,
                this._clanname = e.clanname,
                this._variant = e.variant,
                this._motiveType = e.motiveType,
                this._tonnage = e.tonnage,
                this._tech = e.tech,
                this._omni = e.isOmni,
                this._thrust = e.thrust,
                this._sinks = {
                    count: e.sinks,
                    isDHS: e.hasDHS
                },
                this._armor = e.armor,
                this._weapons = [],
                null === (a = e.weapons) || void 0 === a || a.forEach(e => {
                    this.addWeapon(new y(this,e))
                }
                ),
                this._equipment = e.equipment) : (this.motiveType = K.MotiveTypeEnum.ASF,
                this.resetArmor())
            }
            get thrust() {
                return this._thrust || 0
            }
            set thrust(e) {
                !isNaN(+e) && +e >= 0 && (this._thrust = +e)
            }
            get sinks() {
                var e;
                return (null === (e = this._sinks) || void 0 === e ? void 0 : e.count) || 0
            }
            set sinks(e) {
                !isNaN(+e) && +e >= 0 && (this._sinks.count = +e)
            }
            get hasDHS() {
                var e;
                return null === (e = this._sinks) || void 0 === e ? void 0 : e.isDHS
            }
            set hasDHS(e) {
                this._sinks.isDHS = !!e
            }
            resetArmor() {
                this._armor = {},
                Object.keys(K.ArmorLocationEnum).forEach(e => {
                    this._armor[K.ArmorLocationEnum[e]] = 1
                }
                ),
                this._armor[K.ArmorLocationEnum.FU] = 0
            }
            get damageThreshold() {
                let e = (this._armor[K.ArmorLocationEnum.LW] + this._armor[K.ArmorLocationEnum.RW]) / 2 + this._armor[K.ArmorLocationEnum.N] + this._armor[K.ArmorLocationEnum.A]
                  , a = Math.round(e / 30);
                return Math.max(a, 1)
            }
            get supportedImports() {
                return [A.ImportTypeEnum.MML]
            }
            get allowedTonnage() {
                return this.motiveType === K.MotiveTypeEnum.ASF ? this._tonnages : this._tonnages.slice(0, 10)
            }
            get structure() {
                return Object.seal({
                    FU: Math.max(this._thrust, Math.floor(.1 * this._tonnage))
                })
            }
            get destinyMove() {
                return "" + this._thrust
            }
            get destinyTMM() {
                return "" + (this.tmm(this._thrust) + 1)
            }
            get destinySinks() {
                var e = this.hasDHS ? 2 * this.sinks : this.sinks;
                return Math.round(Number(e || 0) / 5)
            }
            get movePoints() {
                return this.thrust
            }
            set movePoints(e) {
                this.thrust = e
            }
            get typeName() {
                return (this.motiveType === K.MotiveTypeEnum.CF ? "Conventional " : "Aerospace ") + (this.isOmni ? "Omni" : "") + "Fighter"
            }
            get motiveTypes() {
                return K.MotiveTypeEnum
            }
            get destinyLocations() {
                return Object.keys(K.ArmorLocationEnum).map(e => K.ArmorLocationEnum[e])
            }
            clone() {
                return new K(this)
            }
            destinyArmorValue(e) {
                return Object.values(this.destinyLocations).includes(e) ? Math.max(Math.round(this.armor[e] / 4), 1) : 0
            }
            destinyStructureValue(e) {
                return Math.max(Math.round(this.structure.FU / 3), 1)
            }
            weaponArc(e) {
                return [K.LocationEnum.N, K.LocationEnum.RW, K.LocationEnum.LW].includes(e) ? A.WeaponArcEnum.Front : [K.LocationEnum.A, K.LocationEnum.RWR, K.LocationEnum.LWR].includes(e) ? A.WeaponArcEnum.Rear : A.WeaponArcEnum.Any
            }
        }
        K.MotiveTypeEnum = Object.seal({
            ASF: "Aerospace",
            CF: "Conventional"
        }),
        K.LocationEnum = Object.seal({
            N: "N",
            LW: "LW",
            RW: "RW",
            A: "A",
            LWR: "LW (R)",
            RWR: "RW (R)",
            FU: "FU"
        }),
        K.ArmorLocationEnum = Object.seal({
            N: "N",
            LW: "LW",
            RW: "RW",
            A: "A",
            FU: "FU"
        });
        class Y extends n.Component {
            render() {
                const e = this.props.unit
                  , a = this.props.onChange
                  , t = this.props.errors;
                return (0,
                b.jsx)(c.A, {
                    className: "pt-2",
                    children: (0,
                    b.jsxs)(c.A.Body, {
                        children: [(0,
                        b.jsxs)(r.A.Row, {
                            className: "justify-content-center",
                            children: [(0,
                            b.jsx)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.LS",
                                xs: 4,
                                children: (0,
                                b.jsx)(r.A.Label, {})
                            }), (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.N",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Nose"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[K.ArmorLocationEnum.N],
                                    isInvalid: !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            }), (0,
                            b.jsx)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.RS",
                                xs: 4,
                                children: (0,
                                b.jsx)(r.A.Label, {})
                            })]
                        }), (0,
                        b.jsxs)(r.A.Row, {
                            className: "justify-content-center",
                            children: [(0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.LW",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Left Wing"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[K.ArmorLocationEnum.LW],
                                    isInvalid: !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            }), (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.RW",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Right Wing"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[K.ArmorLocationEnum.RW],
                                    isInvalid: !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            })]
                        }), (0,
                        b.jsx)(r.A.Row, {
                            className: "justify-content-center",
                            children: (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "armor.A",
                                xs: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Aft"
                                }), (0,
                                b.jsx)(r.A.Control, {
                                    type: "number",
                                    value: e.armor[K.ArmorLocationEnum.A],
                                    isInvalid: !!t.armor,
                                    onChange: a,
                                    disabled: e.isBlank,
                                    size: "sm"
                                }), (0,
                                b.jsx)(r.A.Control.Feedback, {
                                    type: "invalid",
                                    children: t.armor
                                })]
                            })
                        })]
                    })
                })
            }
        }
        const Z = Y;
        class $ extends n.Component {
            render() {
                const e = this.props.unit
                  , a = this.props.onChange
                  , t = this.props.onAddItem
                  , n = this.props.onRemoveItem
                  , i = this.props.onChangeItem
                  , m = this.props.onSortItems
                  , c = this.props.onGroupWeapons
                  , u = this.props.onClearItems
                  , h = this.props.errors;
                return (0,
                b.jsxs)(b.Fragment, {
                    children: [(0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "chassis",
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Chassis"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "text",
                                value: e.chassis,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "variant",
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: e.isOmni ? "Config" : "Variant"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "text",
                                value: e.variant,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "tonnage",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Tonnage"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.tonnage,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), e.allowedTonnage.map(e => (0,
                                b.jsx)("option", {
                                    value: e,
                                    children: e
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "tech",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Tech"
                            }), (0,
                            b.jsxs)(r.A.Control, {
                                as: "select",
                                value: e.tech,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm",
                                custom: !0,
                                children: [(0,
                                b.jsx)("option", {
                                    disabled: !0
                                }), Object.keys(A.TechEnum).map(e => (0,
                                b.jsx)("option", {
                                    value: A.TechEnum[e],
                                    children: A.TechEnum[e]
                                }, e))]
                            })]
                        }), (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "isOmni",
                            xs: 6,
                            sm: 4,
                            children: [(0,
                            b.jsx)(r.A.Label, {}), (0,
                            b.jsx)(r.A.Check, {
                                label: "Omni-tech",
                                type: "checkbox",
                                value: e.isOmni,
                                disabled: e.isBlank,
                                checked: e.isOmni,
                                onChange: a,
                                className: "ml-3",
                                custom: !0
                            })]
                        })]
                    }), (0,
                    b.jsxs)(r.A.Row, {
                        children: [(0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            controlId: "thrust",
                            xs: 6,
                            sm: 3,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Safe Thrust"
                            }), (0,
                            b.jsx)(r.A.Control, {
                                type: "number",
                                value: e.thrust,
                                isInvalid: !!h.thrust,
                                disabled: e.isBlank,
                                onChange: a,
                                size: "sm"
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: h.thrust
                            })]
                        }), e.motiveType === K.MotiveTypeEnum.ASF && (0,
                        b.jsxs)(r.A.Group, {
                            as: s.A,
                            xs: 12,
                            sm: 6,
                            children: [(0,
                            b.jsx)(r.A.Label, {
                                children: "Heat Sinks"
                            }), (0,
                            b.jsxs)(r.A.Row, {
                                children: [(0,
                                b.jsx)(r.A.Group, {
                                    controlId: "sinks",
                                    as: s.A,
                                    children: (0,
                                    b.jsx)(r.A.Control, {
                                        type: "number",
                                        value: e.sinks,
                                        isInvalid: !!h.sinks,
                                        disabled: e.isBlank,
                                        onChange: a,
                                        size: "sm"
                                    })
                                }), (0,
                                b.jsx)(r.A.Group, {
                                    controlId: "hasDHS",
                                    as: s.A,
                                    children: (0,
                                    b.jsx)(r.A.Check, {
                                        label: "Double",
                                        type: "checkbox",
                                        value: e.hasDHS,
                                        checked: e.hasDHS,
                                        disabled: e.isBlank,
                                        onChange: a,
                                        className: "ml-3",
                                        custom: !0
                                    })
                                })]
                            }), (0,
                            b.jsx)(r.A.Control.Feedback, {
                                type: "invalid",
                                children: h.sinks
                            })]
                        })]
                    }), (0,
                    b.jsx)(r.A.Row, {
                        children: (0,
                        b.jsx)(s.A, {
                            xs: 12,
                            children: (0,
                            b.jsxs)(l.A, {
                                defaultActiveKey: "loadout",
                                id: "unitTabs",
                                className: "h6 m-0 mt-3",
                                transition: !1,
                                children: [(0,
                                b.jsx)(o.A, {
                                    eventKey: "loadout",
                                    title: "Loadout",
                                    children: (0,
                                    b.jsx)(E, {
                                        unit: e,
                                        onAdd: t,
                                        onRemove: n,
                                        onChange: i,
                                        onSort: m,
                                        onGroup: c,
                                        onClear: u,
                                        errors: h
                                    })
                                }), (0,
                                b.jsx)(o.A, {
                                    eventKey: "armor",
                                    title: "Armor",
                                    children: (0,
                                    b.jsx)(Z, {
                                        unit: e,
                                        onChange: a,
                                        errors: h
                                    })
                                })]
                            })
                        })
                    })]
                })
            }
        }
        const ee = $;
        class ae extends n.Component {
            constructor() {
                super(...arguments),
                this.getDestiny = () => null != localStorage.getItem("destiny") && localStorage.getItem("destiny").includes('"isDestinyEnabled":true'),
                this.getDestinyInverse = () => 1 != this.getDestiny()
            }
            render() {
                const e = this.props.unit
                  , a = this.props.onChange;
                return (0,
                b.jsxs)(c.A, {
                    children: [(0,
                    b.jsxs)(c.A.Header, {
                        children: [(0,
                        b.jsxs)("div", {
                            className: "d-flex",
                            children: [(0,
                            b.jsx)("span", {
                                className: "h5 my-auto",
                                children: "Unit Data"
                            }), (0,
                            b.jsx)("span", {
                                className: "ml-auto",
                                children: (0,
                                b.jsx)(i.A, {
                                    onClick: this.props.onReset,
                                    size: "sm",
                                    children: "Reset"
                                })
                            })]
                        }), (0,
                        b.jsx)(r.A.Text, {
                            muted: !0,
                            children: "Use Total Warfare data (record sheets) for input."
                        })]
                    }), (0,
                    b.jsxs)(c.A.Body, {
                        children: [(0,
                        b.jsxs)(r.A.Row, {
                            children: [(0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "type",
                                xs: 6,
                                sm: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Unit Type"
                                }), (0,
                                b.jsxs)(r.A.Control, {
                                    as: "select",
                                    value: e.type,
                                    onChange: a,
                                    size: "sm",
                                    custom: !0,
                                    children: [(0,
                                    b.jsx)("option", {
                                        disabled: !0
                                    }), Object.getOwnPropertyNames(A.UnitTypeEnum).map(e => (0,
                                    b.jsx)("option", {
                                        value: A.UnitTypeEnum[e],
                                        children: A.UnitTypeEnum[e]
                                    }, e))]
                                })]
                            }), (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "motiveType",
                                xs: 6,
                                sm: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {
                                    children: "Motive Type"
                                }), (0,
                                b.jsxs)(r.A.Control, {
                                    as: "select",
                                    value: e.motiveType,
                                    onChange: a,
                                    size: "sm",
                                    custom: !0,
                                    children: [(0,
                                    b.jsx)("option", {
                                        disabled: !0
                                    }), Object.getOwnPropertyNames(e.motiveTypes).map(a => (0,
                                    b.jsx)("option", {
                                        value: e.motiveTypes[a],
                                        children: e.motiveTypes[a]
                                    }, a))]
                                })]
                            }), (0,
                            b.jsxs)(r.A.Group, {
                                as: s.A,
                                controlId: "isBlank",
                                xs: 12,
                                sm: 4,
                                children: [(0,
                                b.jsx)(r.A.Label, {}), (0,
                                b.jsx)(r.A.Check, {
                                    label: "Blank Unit Record",
                                    type: "checkbox",
                                    value: e.isBlank,
                                    checked: e.isBlank,
                                    onChange: a,
                                    className: "ml-3",
                                    custom: !0
                                })]
                            })]
                        }), (e => {
                            switch (e) {
                            case A.UnitTypeEnum.BM:
                                return (0,
                                b.jsx)(q, {
                                    unit: this.props.unit,
                                    onChange: this.props.onChange,
                                    onAddItem: this.props.onAddItem,
                                    onRemoveItem: this.props.onRemoveItem,
                                    onChangeItem: this.props.onChangeItem,
                                    onSortItems: this.props.onSortItems,
                                    onGroupWeapons: this.props.onGroupWeapons,
                                    onClearItems: this.props.onClearItems,
                                    errors: this.props.errors
                                });
                            case A.UnitTypeEnum.AF:
                                return (0,
                                b.jsx)(ee, {
                                    unit: this.props.unit,
                                    onChange: this.props.onChange,
                                    onAddItem: this.props.onAddItem,
                                    onRemoveItem: this.props.onRemoveItem,
                                    onChangeItem: this.props.onChangeItem,
                                    onSortItems: this.props.onSortItems,
                                    onGroupWeapons: this.props.onGroupWeapons,
                                    onClearItems: this.props.onClearItems,
                                    errors: this.props.errors
                                });
                            case A.UnitTypeEnum.CV:
                                return (0,
                                b.jsx)(G, {
                                    unit: this.props.unit,
                                    onChange: this.props.onChange,
                                    onAddItem: this.props.onAddItem,
                                    onRemoveItem: this.props.onRemoveItem,
                                    onChangeItem: this.props.onChangeItem,
                                    onSortItems: this.props.onSortItems,
                                    onGroupWeapons: this.props.onGroupWeapons,
                                    onClearItems: this.props.onClearItems,
                                    errors: this.props.errors
                                });
                            case A.UnitTypeEnum.BA:
                                return (0,
                                b.jsx)(H, {
                                    unit: this.props.unit,
                                    onChange: this.props.onChange,
                                    onAddItem: this.props.onAddItem,
                                    onRemoveItem: this.props.onRemoveItem,
                                    onChangeItem: this.props.onChangeItem,
                                    onSortItems: this.props.onSortItems,
                                    onGroupWeapons: this.props.onGroupWeapons,
                                    onClearItems: this.props.onClearItems,
                                    errors: this.props.errors
                                });
                            case A.UnitTypeEnum.IN:
                                return (0,
                                b.jsx)(_, {
                                    unit: this.props.unit,
                                    onChange: this.props.onChange,
                                    onAddItem: this.props.onAddItem,
                                    onRemoveItem: this.props.onRemoveItem,
                                    onChangeItem: this.props.onChangeItem,
                                    onSortItems: this.props.onSortItems,
                                    onGroupWeapons: this.props.onGroupWeapons,
                                    onClearItems: this.props.onClearItems,
                                    errors: this.props.errors
                                });
                            default:
                                return "Unit type not yet supported."
                            }
                        }
                        )(this.props.unit.type)]
                    })]
                })
            }
        }
        const te = ae
          , ne = [13, 12, 6, 5, 4, 4, 3, 3, 2, 1, 0]
          , se = [13, 12, 6, 6, 5, 5, 4, 3, 2, 1, 0]
          , re = [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
        class ie {
            constructor(e) {
                null == this._pilotBlank && null == e && (this._pilotBlank = !0),
                this.setDefaults(e)
            }
            get pilotBlank() {
                return this._pilotBlank
            }
            set pilotBlank(e) {
                this._pilotBlank !== e && (this._pilotBlank = e,
                this.setDefaults(this))
            }
            get methodData() {
                return ie.pilotMethods[this._method]
            }
            get method() {
                return this._method
            }
            set method(e) {
                this._method !== e && (this._method = e,
                this.setDefaults(this))
            }
            get gunneryTW() {
                if (this.pilotBlank)
                    return "";
                if ("destiny" === this.method) {
                    let e = Math.min(Math.max(+this.reflexes + +this.gunnery, 1), 11);
                    return ne[e]
                }
                return this.gunnery
            }
            get gunneryCost() {
                return this.methodData.gunneryScores[this.gunnery] - Number(this.reflexes)
            }
            get pilotingTW() {
                if (this.pilotBlank)
                    return "";
                if ("destiny" === this.method) {
                    let e = Math.min(Math.max(+this.reflexes + +this.piloting, 0), 11);
                    return se[e]
                }
                return this.piloting
            }
            get pilotingCost() {
                return this.methodData.pilotingScores[this.piloting] - Number(this.reflexes)
            }
            get tacticsTW() {
                if (this.pilotBlank)
                    return "";
                if ("destiny" === this.method) {
                    let e = Math.min(Math.max(+this.tactics + +this.intelligence, 0), 10);
                    return re[e]
                }
                return this.tactics
            }
            get gutsTW() {
                if (this.pilotBlank)
                    return "";
                if ("destiny" === this.method) {
                    let e = Math.min(Math.max(+this.guts + +this.willpower, 0), 10);
                    return re[e]
                }
                return this.guts
            }
            get leadershipTW() {
                if (this.pilotBlank)
                    return "";
                if ("destiny" === this.method) {
                    let e = Math.min(Math.max(+this.leadership + +this.charisma, 0), 10);
                    return re[e]
                }
                return this.leadership
            }
            get attributesCost() {
                return this.pilotBlank ? "" : +this.strength - 1 + (+this.reflexes - 1) + (+this.intelligence - 1) + (+this.willpower - 1) + (+this.charisma - 1) + 2 * (+this.edge - 1)
            }
            get attributesLevel() {
                return this.pilotBlank,
                ""
            }
            get skillsCost() {
                return this.pilotBlank,
                ""
            }
            get skillsLevel() {
                return this.pilotBlank ? "" : Number(this.gunneryTW) + Number(this.pilotingTW) >= 10 ? "Green" : Number(this.gunneryTW) + Number(this.pilotingTW) >= 8 ? "Regular" : Number(this.gunneryTW) + Number(this.pilotingTW) >= 6 ? "Veteran" : Number(this.gunneryTW) + Number(this.pilotingTW) >= 4 ? "Elite" : "Hero"
            }
            get skillsRank() {
                return this.pilotBlank ? "" : Number(this.gunneryTW) + Number(this.pilotingTW) >= 10 ? 1 : Number(this.gunneryTW) + Number(this.pilotingTW) >= 8 ? 2 : Number(this.gunneryTW) + Number(this.pilotingTW) >= 6 ? 3 : Number(this.gunneryTW) + Number(this.pilotingTW) >= 4 ? 4 : 5
            }
            setDefaults(e) {
                this._method = (null === e || void 0 === e ? void 0 : e.method) || this.method || ie.CreationMethodEnum.DFA;
                let a = this.methodData.startingScores;
                null !== e && void 0 !== e && e.pilotBlank || this.pilotBlank ? (this._pilotBlank = !0,
                this.pilotName = "",
                this.strength = a.strengthMax,
                this.reflexes = "",
                this.intelligence = "",
                this.willpower = "",
                this.charisma = "",
                this.edge = a.edgeMax,
                this.gunnery = "",
                this.piloting = "",
                this.tactics = "",
                this.guts = "",
                this.leadership = "") : (this._pilotBlank = (null === e || void 0 === e ? void 0 : e._pilotBlank) || !1,
                this.pilotName = (null === e || void 0 === e ? void 0 : e.pilotName) || "",
                this.strength = (null === e || void 0 === e ? void 0 : e.strength) || a.strength,
                this.reflexes = (null === e || void 0 === e ? void 0 : e.reflexes) || a.reflexes,
                this.intelligence = (null === e || void 0 === e ? void 0 : e.intelligence) || a.intelligence,
                this.willpower = (null === e || void 0 === e ? void 0 : e.willpower) || a.willpower,
                this.charisma = (null === e || void 0 === e ? void 0 : e.charisma) || a.charisma,
                this.edge = (null === e || void 0 === e ? void 0 : e.edge) || a.edge,
                this.gunnery = (null === e || void 0 === e ? void 0 : e.gunnery) || a.gunnery,
                this.piloting = (null === e || void 0 === e ? void 0 : e.piloting) || a.piloting,
                this.tactics = (null === e || void 0 === e ? void 0 : e.tactics) || a.tactics,
                this.guts = (null === e || void 0 === e ? void 0 : e.guts) || a.guts,
                this.leadership = (null === e || void 0 === e ? void 0 : e.leadership) || a.leadership)
            }
            clone() {
                return new ie(this)
            }
        }
        ie.CreationMethodEnum = Object.seal({
            DFA: "dfa",
            Destiny: "destiny"
        }),
        ie.pilotMethods = {
            dfa: {
                name: "DFA Rules",
                startingScores: {
                    strength: 2,
                    strengthMax: 2,
                    reflexes: 4,
                    intelligence: 2,
                    willpower: 2,
                    charisma: 2,
                    edge: 1,
                    edgeMax: 1,
                    gunnery: 4,
                    piloting: 5,
                    leadership: 0,
                    tactics: 0,
                    guts: 0
                },
                gunneryScores: {
                    5: 4,
                    4: 5,
                    3: 6,
                    2: 8,
                    1: 9,
                    0: 10
                },
                pilotingScores: {
                    6: 4,
                    5: 5,
                    4: 6,
                    3: 7,
                    2: 8,
                    1: 9,
                    0: 10
                }
            },
            destiny: {
                name: "Destiny RPG",
                startingScores: {
                    strength: 2,
                    strengthMax: 6,
                    reflexes: 1,
                    intelligence: 1,
                    willpower: 1,
                    charisma: 1,
                    edge: 1,
                    edgeMax: 6,
                    gunnery: 3,
                    piloting: 3,
                    leadership: 0,
                    tactics: 0,
                    guts: 0
                },
                gunneryScores: {
                    8: 0,
                    7: 1,
                    6: 2,
                    5: 3,
                    4: 4,
                    3: 6,
                    2: 8,
                    1: 9,
                    0: 10
                },
                pilotingScores: {
                    8: 0,
                    7: 1,
                    6: 2,
                    5: 4,
                    4: 6,
                    3: 7,
                    2: 8,
                    1: 9,
                    0: 10
                }
            }
        },
        ie.attributeScores = [1, 2, 3, 4, 5, 6],
        ie.skillScores = [0, 1, 2, 3, 4, 5, 6];
        const le = ie;
        n.Component;
        var oe = t(2803)
          , me = t(2970)
          , ce = t.n(me)
          , ue = t(1412)
          , he = t(1700)
          , de = t.n(he);
        const ge = t.p + "static/media/card-base.10b6f01d7617412d1d24.png"
          , pe = t.p + "static/media/mech-bp.92838a1bec17e2d3f6b5.png"
          , ye = t.p + "static/media/mech-qd.9757a4c94b199d37c8a5.png"
          , xe = t.p + "static/media/vehicle.aea9b992ee04dad50cfc.png"
          , ve = t.p + "static/media/vehicle-turret.5beb2600a097c800abb4.png"
          , Ae = t.p + "static/media/vehicle-treads.b407af8cadcdcc275192.png"
          , Me = t.p + "static/media/vehicle-wheels.809268bb733788834e3f.png"
          , Le = t.p + "static/media/vtol.4b9f46420113004b86c1.png"
          , fe = t.p + "static/media/aero.f4dc17e1c9ded8b2182d.png"
          , Se = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAQAAADa613fAAAACXBIWXMAAC4jAAAuIwF4pT92AAAEI0lEQVR42u2ceWhUVxSHv5kYjUstCRo1pNYtjpEoLtXYog1FbbRiREURjSiKC1gXCC1tXWi0UqLS1i60ohKLYjWIoqgoVrBp4xY3jHEZtVE0EKxpDGnqkpjxD6O+GyYz7915mbzI+c1/791z7v3effecew8z48K/enEKZyqZq/4uN6unuYu2DgVx+b/s5jVRsyD371LkkJF2JV7HLBEfPnysdcwjX1s7osTX/NUSEAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREAEREH+KDC/IR0wL+p1h6/KwlfTwgsSzjfNMIsI2iASyuUh6uGcEIIkc8kmzAaYbmyhgJs0bb430Zy95jK7vq/cm9DY/U8hsWjT+Yk/mALl8oAETz49cYT5RTolaLoZylCMMs2ATx3dcYwEtnRZ+XQznGIcYbGJmOrIOL4tp5dQ84iaVE+xhQIA2sWThJYPWTk+IbsZxmhyS/Nxrx2q8fMobTSWzRzCJc2zDY7gWQyZevuDNprZFiWQaBWymOxDNcq6zguiG29nobjMq8ZlY1JHMYioHSKGdSb93KAzvjGxnJHmmWkYx0SRGMYvxmPRqG4iPo7zPGPJtejNKyMDD9zxsjDVSw0GGMIELIULc4zN68g2VjbnYa9jDIKZwWdO+lGX0JIsKJ0StanbSj5ncsGj3L5kksJpyJ4XfKn4libncNtm+nK/w8CVl4cojPgu+HrORRBZRHKRdBVkksJz7FsOLll78MrRI40jbhgxKau3rfv5jHR01st10igL/MjQYiA8fBUy0fApsy1Lu14GoZD1xGhBTKDR4sQgSSy41BvOzjLW8nqLJ5EGt/UN+4i2tPdtFwyhq+INY6+eLUZxQnuhxUi2fAtuTxT020EUDYjznlf7/YqTukTqCNM7VeSIplp1FaYSgNM4o/Z5kVKgRNoLJXFKezGHea7hdLG7GcFLpL580u9JEJOl4Da6fsp+BIVRO6of4kOPK2rzAeBtrZwC0YA5/G7qoZhd9bfTvYgS5ykwUMNluiBdqyQLuGrqqYju9bIFI4ZgyE1eY2gAl2YDp7gnZdA/J4zCOKDPhZYZu4dSq6qa7R/xCZ62ZeJfDPDV4usnsUAqnOophJWUh5e1k9iuv0y3m2VFz1FEsa6gwDKWCNSYz70D2UW2wvMPHdtUcdRXHev43DOkBq4gJaNGf3QpEMUvsLtfpqjMbeGQYWilL66lf9SGHKkPLEj6hDY5SD7J5EnCIvflNgfiHz536D0WJ7FCGWszC2jffw1YFs5QVDVVztEv92K0E1FssYguPDVfKyAyyihwiF+9wUIF59Snna9NVR4doKL8rWeJ5cO5AE5SL4fz58qz+LZ1ownIzmjx+0PtvLCt6BrRivfyM+W9XAAAAAElFTkSuQmCC"
          , be = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAQAAADa613fAAAACXBIWXMAAC4jAAAuIwF4pT92AAAFnklEQVR42u2ce1AVVRjAf/cC+cgsGEVzyDRFoHyjkoo5Jj5QIZHRGDRzKm0aTZuYmsw0qbRB7WHmlGVDjo4mYzglmqY4PhEw0QEVvWTYIDOOScoQ+eCx/SHSLnOXu7t3996Lnu/+d/a8fnvO933n+/bMteFcwsnDNyWKc86K/VWq22jvoyA258V27hHxd/H8EqU+MtPuhBhpFoGEhMRKn3nlKxtmFHGPby0BIkAEiAARIAJEgAgQASJABIgAESACRIAIEAEiQASIABEgAkSACBABcp+BWPUC/Ojo2Qkls4rOpkNMoYAEz4K0JYXzLKeDaTtjMvn8SF9v6Eh7FuLgfR5xG2IieWQy0JvKHshSSlho+J6EjViOkMUgtRsNnlTaDizHwZu00z12DIfZyVBfMr+d+IRi5tFG80qMYj+/MtzdlbDCjIawhrPMppVLiBHsI5uRZkFY4Q+68Q2nmUWAKsQwdnOQZ82EsMqx9SSdQpKcXNiJIosjjDUbwkoPHc4WTpCIX2NJJDvIYYIVEFaftfqyjTwmYWcAmeQzycrR/A22K6OaBzXUi2QHJXTXOI5ELjmeXZFfCGctNzTVDdWIkUccwznt6a11iXk8xXpum7AvJE4Qx3B2InlHR0qZTW82UuNWLwUkMoQs6ryr7CXMZAAZBqdRSCJRbKfeN6zWGZ5nMD/pnE4RSQwkk1rfMr8nSWAouzXCFJNMJFvd205W+RGJfGIZxX4X9c4xk35sUdGsAM+CTGC6ilE9RAwx5KjYnxJm0U/VPISxkRmeBQlhEyeZKjuCyFcmm2jiyG9SfoFX6MMGFYMdSjqFzDC6Imri6gLznIbnBcQ7hbmTTJjMqYZ6pc0e759gPTcbas5RqePiArO7IBISucSqHgX9SeIAr9FadaTH+Yobst68CCJRz2FGGTjXhvAl/yp6MgxijtWyEU02exmho00XPuc8czUHxx4zvzZGc4DdDNGwMp1ZhYMFtPXVeMTOOI6xvdkMVTBpOEjRFAR4NbCy8xz5ZNDbaeJoGQ7e5qGWEiH6MZUCNhEmKwsiFQfv8nBLC3UDmE4R39EDCGQxJSwh0PdC3WokDUodwEsks5ORmpPdZZzx7IpsZgxHNdVsTaJGjHIWEKaxV9NAJLJ5hokcN2lnXCaFML7QmAUwWUfq2cXTTOGUmxBXeIdefEq1N5W9nu0MJomzBttX8B69SKPKF6xWLVvpzyx+19nub1IJZRmVvmR+a9hAb+bwp8b6lXxEGEu55ik/oifPdItviWA+5S7qVZFGKIu5qtO8uBVYlaqGtOrSjhQuNzmc3/39Y+hrsD8vUOpePCIhUaTIqmuT9iziahOIalbTxQBEEmdkvegECeYQ9bLmJ4jTrU+BpHK9of0N1vKYoTNboSKAO0iw/vhiPMcUbzSHcbqjwI6kcYV1dDMAkcBJxfhHGGP064of8RQ0eSP6v/y1NmCC4vlNMW4u4921sH5M47TizexhmHWnWOxMJFcx3nHizXITAczAIeu6jiwiLfiIZmcsOQrdPEWCbkPjQloxmz9kQ9SyzfjNEac6GcMhxUoUMc1siLvShrlckg1Vw2bCTYEYyQHFShSTbDhWMujubpNOD7d6HMFexUo4eNHsxKlWd3eTr+lqaCWGsoc6WU8XeJkH8KgE8QHX3PLbUWQpttNFXjVgqk2RYFZQJZtKFSs0et5IfqZW1rJMx4Uci6QLqxX52+t8SFCzLQaQqYAo5w2z03VGpSvrGj8LSEhUsEglf9WHDGpkNS/zlu57XhZLT9K53ewUn2SLAuIvN27eWSwR/KCYajmvN+z8MDYqMCtYYlXO0SzpT6bCoF5kPt9zS1ZyjVQXWuQjYmMQuxQw//8q+di0K7Yekmj2KbzEHePciRYoNkZzuDFW/4xHacFiJ5ajrDH231h65D9yPF5eocZw1gAAAABJRU5ErkJggg=="
          , Ce = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAQAAADa613fAAAACXBIWXMAAC4jAAAuIwF4pT92AAAF6ElEQVR42u2ce0yVdRjHP+cAiWYWDtEcmaYIlHdU8pYz8YIIiUxjaOYybU3TFqtlpkmlDbWLmSvLRk6nyQxXgmGK84IIGOhAvBw0bMrmvDMiLyBv/yCdl533nPd6zot7n/e/3/ndvu/ze57n931+v/fYcC0RFGFOieaMq2J/ieo2OpgUiM11sZ2HRPw9/H6JKpPMtAehappFIiAgsNo0r3x104wiH/KlZQGxgFhALCAWEAuIBcQCYgGxgFhAfPUC/Ojk3QmlsIYuuoOYSimJ3gXSjlTOspJg3VbGFIr5hX6+sJEOLMbBRzyhGUQcRWQxyJfGHsRyKlmsOnlkI5Z8shkslebxptEGsxIH79Be8dgxHCaHYWZyv535nNMsoK1sTYxhP38wQqsmjHCjoazjFHNp4xHEKPaRx2i9QBgRD7rzPSeZTYAkiOHkcpAX9QRhVGDrRQZlJLvIYkaTTT7j9QZhZISOYBslJOHXXBLFLgqYZAQIo/da/dhBEZOxM5Asipls5Gj+KttdpI5HZdSLYheV9JA5jkAhBd7VyO9EsJ7bsuqGyYRRRDwjOOntpXWJBTzHRu7psC4ESohnBDkIvrGRKubSh83Ua+qllCSGks193xp7JbMYSKbKaZSRRDQ7aTSH16rgZYbwq8LplJPMILJoMJf7PU4iw8iVCeY0KUSxXdtyMorqChQTyxj2e2h7hln0Z5tLyzIR1T1EDDEUSPifSmbTX8I9aKK6UuLpMHQeAjVuqK6NOIqa+njwnGOO5M7YzhRKEBCYJ1HDw2GoFiACAjfcUF0/pnCiqV6Vm+29nTiO0dhU00dABASuuqG6/iRzgDcJdEN1C0R68yEQAYHLKqlufrMmNAKxqK5FdS2qa1Fdi+paVNeiuhbVtaiuRXW9Gkf0oLpIbm4MAjKJGRJOVT3VhXA2M9O7QELZwnGmOW1BnDWTx0jiKW5Rfp7X6csmCYcdRgZlzFSrEa3EqpQEl2CUUF14ho3c8T1DLCRWcivoierC03zLbbNQ3UYOM0bFvjaUb/jXTFTXxkjy2MsoBW268hVnmS+bHHvN/doYywFyGSpDM11Yg4NFtDMrH7EzgaPsdHsZI4R0HKTKIgE+JVZ2XqKYTPq4+C2YFTh4j8daC0P0YxqlbCHcqawjaTj4gMdbG9UNYAbl/EhPIIilVLKMIPNR3ToEGUYdwGukkMNo2fe6LlLhXY1sZRxHZNUMJEkmjGoWES6zV92ACOTxAnEc02llXCaVcL6WmQXQ2UYa2c3zTOWERhBXeJ/efEGdL429kZ0MIZlTKttf50N6k06tGbxWA9sZwGzOKWx3gzTCWEGNmdxvPZvowzz+llm/hk8JZzk3vRVHlOSZ7vIDkSyk2kO9WtIJYynXFLoXTcSqSpLSSkt7UrncYnP+4PlH1cVnf16hShsfERAoF2XV5UkHlnCtBYg61tJVBYhkKpx6UQgkhEOi070S4hXbUxBp3Gpqf5v1PKVqz1YmInAHCVHOLyZyVPRGC5igmAV2Ip0rbKC7ChCJHBeNn884tacrfiRQ2uKNKD/5C1ThghL4UzRuIRO1elg/pnNS9Gb2MNy4XSx24igUjXeMBL3CRAAzcTh1fZ9sogw4RLMzngKRbZ4gUbGj8SBtmMtfTkM0sEP9RxIubTKGQyJNlDNdbxAPpC3zueQ0VD1bidAFxGgOiDRxmhTVXElluLtHBj019TiKvSJNOHhV78Sp3HB3h+/opkoTw9jDfaeezjOHR/CqdORjbmqK29Fki5bTBd5Q4ap1kRBWUes0lVpWyYy8UfxGg1PLiwou5BgkXVkryt/e4hM6um0xkCwRiGre1jtdp1a6saH5WEBA4DpLJPJXfcmkXnTP613F97wMll5kcM/tFJ9lmwjEVQ0fmRkskfwsmmo1bzWt/HA2i2BeZ5lROUe9ZABZIod6gYX8xF2nkpukebAik4iNwewWgfn/qeEz3b4m9ZKMZF+Li5e1rKIzrVBsjOVwM1f/kidpxWInliOsU/ffWErkP8KXDincIkkMAAAAAElFTkSuQmCC"
          , Te = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAQAAADa613fAAAACXBIWXMAAC4jAAAuIwF4pT92AAAHFElEQVR42u2ceXBNVxzHP+89qaWkZWxVlFqeLYggjURNKoglKoJmQjGKjqV0SjvUUtrSsbVVNWi1ahnKaGiF2mKsIVGJCkFCoxOZUUvFGkRy+4fneTfezbvvLi/3tv1lMu/l3N8953zvOb/f7/yWGwvuqQnJGJOCOeOuuYwEuwV/gwKxuG+28i+hMh6uXyTbIDOtT20ltzVFQEBgnmEe+TzHjJr+y7fW/0C8oFa0Kn1h14L6A7+bf0WsxBCj/zj6A2mJHTsB5gfSDwsW+pkdyGMI/aSOFmYB0prGANhpaW4gj1dC981l1bn3vs7v0fqOpS+QAJo4vzejuRkMYhU6Y8WKzfFrxYaNziKxn8QOBIoch7/Hn2c5aSQg+UQyzANPHHFPtX3PTmNtrXyGM4SbXt1zkyEM55bRZERgFSGkyeZPI4RVCEYT9hcByCCMJRR55C5iCWFkGFFr/eX4vMto4sgrkTePOEZz15jq96HL9/W0KyGYlEw71pvFjpwjnAtur1wgnHNmMojVqOO2vQ7VzGXZo7C5bbcRZS4gfRRcMSCQqoS6/JUhUrShVDUPkEjKOy3GUoIJZqnTupQn0jxAoh2fV4hhFLe5zShiuFLsquGBVCICgJ0EstnZuplAxwExgkrmABKBP/eYSA9yRe259GAi9/B3ADU8kD5kEMYCCp+6UsgCwsjQQ3NpD6QcOQRzTPL6MYLJoZxRPcQnVMBUDxy3mSphLg21IoUachkm+OBD+s8D0esB2JSejpVOKI751NQcRF9Sldp9pUAqMIGzzNbsAGilDyn8pDxCrGaL+DOZTD7iedUgepJMPG1KU9grM4MsJiuuk7DQnYMk0FZt2kELoa3KbDJ5j4pejx3BAbYSYiT1W4MFnGas0w/xvBLh7GEnoVolgLRUo7VZRAYjKOsRREd2k0gnLbNYWtuDenzDSYbiJwmiA9vZx2tap+L0MGwNWcEJYt0cSINJ4CBd9cgn6mWhm7COY8S4nHKD2EISPfRKiup51mrJRpLphZVA4kmhl56jKfVHcrjDszL4gthCFvVljiNwhCTfrsivNGEx+bJ4G8mEkUwUoUoTccoX+yJjac5yHmiwLwSOEUUoW5UnftTt2mxG0ILVFKjqJZUY2pOgzmtUL35ZDCaQDQqncYIYgtkkI8vlE611ijdox89eTiedWNoQL0oSGUD9phFNCNtlgjlNHEGs1y4IoaVmF0ihO+Hs8cB3hsG0Yp2EZPn5FkgPBkoo1f1EEEGShP7JYiitJNWDndUM8i2Q2qwhjf5uA20CiYQRRUqx9vMMJ4CVEgq7ESs4wSClKyJFngqYRzqup9JbMmpoow/HHXzZJR7vX2Y59xycIyV4PBQwqwUiIHCE7pJHwTLEspdRJcR6X2IJ+S69lSIQgSIOEK7gXFubr7kr6kkxEG20loUwEtlFRy/uqcWXnGWMbOfYZ+rXQmf2sp32MlamJvPJZDwVjOqPWOnGYTaVGKGqzhwymSDLCShVx8rK66SwgRZuA0ezyOQDs+QQwUZ/UlmD3aWtCjPJ5EOeM5ur68dA0vmOBkBlppHFdCobz9W9gyBDqP0YRhxb6SQ72J3DKd+uyFq6cEgWZzliZMLIZTx2mb1qBkQgkVfpyVGNdsYlJmDnK5lRAI1lpIhtvEJfjqsEcZlJNOZz7pSmsBexiXbEKi60vMZUGjNHfdGsFlrrIetpzVCvS/z+ZiaNmMUNI6nfAlbSgpH8KZP/Bp9iZwbXfWVHvIkz3edbmjKuWCnN03SLOTRiGle9VC+qHKtsSZdWmioygUvFDuePf24rygaX4U2y1fkjAgLpoqi6PPJnCleLgbjDQmopABHLKZdevARSnf3OFyMER0jTW3mqzEzyHPfns1iigNbTme2EyIHbR3Xv/YtIDoueaBLdvPYCqzGHyyyjngIQ0aSJxj9IF6XZFRu9SS32RLzP/JVToIJ685to3CNEqtWwNgZwUvRkdtBBv1MsVnpyRDTeUXprZSb8GESmS9eFJBCkQxLNSleSRLJ5nGiti9TKMoI/XIZ4yEZN3y20EMF+0UqkM0D7SrtHVJ4xXHQZqoC1Lu+1qQHRib2ilThNnN5vdhc3dw9YQQNVPXZkl2glMhmideBUrrm7x1LqKlqJEHZQ6NLTed7iGXxKVfiY66rsdjAJou10gbe1L6OVa//ncstlKreYK9PyBvELD13uzPGiIEcnqsVCUfw2j0+oUuIdgcSLQOTyrtbhOqVUl2XOtICAwDWmSMSvAthAgQvnJd73us5LZ2rICh6UOMVmrBOBuKKi8k5nasqPoqnm8o5j59tZLYJ5jel6xRy1otbEixTqBcbxA/ddWq4z04MUGYQstGWbCMyTnxt8ps87VvpRGLtFVuKRcq6BCclCZw44ffUveAETk5XuHGKRsv+N5Q39AxFZukTkHiY+AAAAAElFTkSuQmCC"
          , Re = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGQAAABkCAQAAADa613fAAAACXBIWXMAAC4jAAAuIwF4pT92AAAHL0lEQVR42u2ceWxURRzHP7vbcgloCZdcghzbckOBCgUJUqAcrZRyNAWRqGAMCMZGAyJIVTQFPBBBUAg2EBACJUpBKkc4S1ukYEs5WrGY0oRUEJqK5Wqff7Bs9tV9u++Yt7ugv6bp7rz5/ma+b2Z+M7/fzNSCewklm8CUCM67Sw5SyG6hYYASsbhPtvKISJCX55cpDpCatqOVHlgYEhISSwPmlS911CjsEe9a/xORSQ96+A2tcrCrkwnAL35CC2wRK/HE69ZkDC2USHfs2OnmF7RQIuOxYGG8X9ACiTyoxHilxYOJaKFEetIJADvdfY4WSuTBu9TXPYyhBRKxMs75OU6zNmNooUS6Eer83JkuPkXrnBCDiSUIKzbHrxUbNobKBu5cMpCodizvHvy9wBmDaAPy79VvLdY50rT9rKOBYbSK1a+WZbyFqZRrqkY5U51m1RhaKJH7PTlXdUVy6SwQLZgI1GMVVV6rUcUq6rnRqx8tnAjAJK57rMh1JnnQrQ9tChHoQJZiRbLo4EW7HrRJRKAuxW4rUkxdFfq1o03z2ZvQ2m16a5qYjhZKJAab23QbMaajhRIZq+OJKLRAIo2JdPl2lrMu3yJpbCpaKJFo56CsZjURRLCaaudAjjYVLdRqbXc8L3PpCmMpc6Ru96JdD9oU89vAsWrKoKUsvSUZjlVSAw+69aFNIRKHRCVJbiyPjSQqkYjzoFsf2hQiqRQQrogNp4BUD7r1oU2YEOtQQgQnFZ+fJIIS6piCFjrYbao02DSme8tlQotUGcpVJbAMwZHGgJD/PBGzXoDN16vfRJbRXDiJceR6nIFMIFKPJC7wkb4Fntt6jCWH7fojwEa6SEPmUch7PGGYxGiySaO3Pwd7CIsoYp7ucxIWRnKUdPr4f1sBGvMRhbxJfc1lR3GEXfQPJPPbjE84xyxVgYf7LTGEA/xEpNGWMMOMtmIFZ5lOba8kBrGP/QwWRcKM+aAtX3OGaQQrkhjAHg7xnEgSZk1sHVhPHglutiwiSOcow0WTMHOGDmUzJ4l3WcWGs5NMRplBwuy1Vne2kc0YrPQijRzGmFma3iMcJdzkMRX5wtlJEe1UliORRaZvW+RHQllJpaq8HVXSyCaGSL0bbfob+zKz6MJa7gjoFxIniSGSXUj+GSPFTKcrG7hrSEsu8fQjXbtXKHawFzGVXmzVWY084olghzPO6GerVcAk+vK9xurkk0Bv0rgXWOb3FHH0Z49KMudIJJwtxrqTWfOIRA4jGcIBL/nOM5UebFYYWcG+JTKKyQpG9TBRRJGpYH+KmEYPRfNgZwNTfEukFRs5xQS34TaJ/Qwkhpwa6Rd5hW6kKhjsjqwnjyl6W0RJvG0rzHBu68d6iCmO5bRzk9PT8v5p1nLLkXOGQh6TdnVnyDaURyouBYNI4CCveYjlPsVXVLpo8yMRiWqOMETHurYVX/J3jQ1qnUTEWC0LA9nPXgZpwLTgcy4wU7Vz7DPza2EoB9lDPxUt05xlFDLH7WmVgPBHrIzgODs8RqiakkIhSaqcAL86VlaeJ4etdHUbOFpMIW973GEMKA/RxgRy2YjdJa0RyRTyDo8/bK5uMJPJZx3tgRAWUMRCQgLP1b2JpGJQB/MSiexisOpgdwkFvm2RTQzjmKqcdYhXSaOUOdhVahVGRGI/zzKaE4J6xhWSsPOFyiiA4DFSzW6eYRynDZIoYy6d+JSb/hzs1eygLwmy8z1a5Brv0okUKgLBat1jCz2Zxq8acX+STEcWUx5I5vcuqXRlBr+rzF/Oh9hZxHVfzSNa4ky3+YYwZlPqJV8FKXRkAVc1mhdDjlWxokurLPVJ4orCYdi/dO0GB/GC81SqTn9EQiJfFlVXJw2Zz9UaJG6ynBY6SCRQ4KJFI5GmHHZefJAcIU2t4ymEZG448JWsVDgg623Nlidz4A7RVLt/Ec1x2RvNZIRmL7AJKZSxhrY6SMRxSlb+UYbp3V2xESu7X1DNIR07f3V0mKBYfpaVm0W0UQtrYyJnZG8mgwHmrWKxMrrGyfkTxIqaJoKZQqHsWkQ64SZsolkZTqZsbJ4mTrOh8SK1mc5vLkXcY5vRu4M1xmQUh2Utkc9E0SQeSF1mctmlqLtscrm3ZoTEYA7KWuIciYJudque7u6wnvaGNA5ir6wlCnlRdOBU7XR3i9W00dUS/cmQXVW6yMvUwqfSiPdlV4y0z9sRpMu60yVeFXdMVuv8v4QKl6pUsETlzBvOD9xzQZZoOJBjkrRguSx+e4MPaOQR0Ys0GYlS3hAdrtMrbVjj3BaQkLjGfIX4VTe2ctcl5xXe0nzOy2TpwHrueKxiZzbLSPxh4OSdyRLGd7KqlvK6o+fb2SCjeY2FZsUcRUlP0mQG9RKz+ZbbsguTyV5GUYCIhT7sVrjIWs7Hwo7Y+kgGsk82S9w3zs14CMXCUI44ffXPeJKHWKyM5Bgr9P1vLC3yD7WAO8QgR8SxAAAAAElFTkSuQmCC"
          , je = 36
          , we = 28
          , Ee = 15
          , Be = {
            x: 60,
            y: 60
        }
          , Pe = {
            x: 60,
            y: 150
        }
          , ke = {
            x: 60,
            y: 215
        }
          , Ie = {
            x: 170,
            y: 215
        }
          , Fe = {
            x: 60,
            y: 265
        }
          , qe = {
            x: 170,
            y: 265
        }
          , Xe = {
            x: 60,
            y: 335
        }
          , Ne = {
            x: 170,
            y: 335
        }
          , We = {
            x: 60,
            y: 385
        }
          , ze = {
            x: 170,
            y: 385
        }
          , Ge = {
            x: 440,
            y: 335
        }
          , Oe = {
            x: 545,
            y: 335
        }
          , De = {
            x: 650,
            y: 365
        }
          , Ue = {
            x: 707,
            y: 161
        }
          , He = {
            x: 707,
            y: 206
        }
          , Ve = {
            x: 707,
            y: 251
        }
          , Je = {
            x: 707,
            y: 296
        }
          , Qe = {
            x: 707,
            y: 341
        }
          , _e = {
            x: 707,
            y: 386
        }
          , Ke = {
            x: 60,
            y: 452
        }
          , Ye = {
            x: 68,
            y: 505
        }
          , Ze = {
            x: 420
        }
          , $e = {
            x: 420
        }
          , ea = {
            x: 635
        }
          , aa = {
            x: 635
        }
          , ta = {
            x: 690
        }
          , na = {
            x: 690
        }
          , sa = {
            x: 830
        }
          , ra = {
            x: 830
        }
          , ia = {
            x: 890
        }
          , la = {
            x: 890
        }
          , oa = {
            x: 950
        }
          , ma = {
            x: 950
        }
          , ca = {
            x: 1010
        }
          , ua = {
            x: 1010
        }
          , ha = {
            x: 1070
        }
          , da = {
            x: 1070
        }
          , ga = {
            x: 60,
            y: 1145
        }
          , pa = {
            x: 230,
            y: 1145
        }
          , ya = 60
          , xa = {
            x: 610,
            y: 1070
        }
          , va = (new Set([6, 5]),
        new Set([6, 5, 2, 1]),
        new Set([6, 5]),
        new Set([4, 3]),
        new Set([4, 3]),
        new Set([6, 5, 4]),
        new Set([6, 5, 4, 1]),
        new Set([6, 5, 4]),
        new Set([3, 2]),
        new Set([3, 2]),
        {
            labels: {
                HD: {
                    x: 1460,
                    y: 215,
                    text: "Head (12)"
                },
                LA: {
                    x: 1200,
                    y: 270,
                    text: "Left Arm\n(10,11)"
                },
                RA: {
                    x: 1720,
                    y: 270,
                    text: "Right Arm\n(3,4)"
                },
                T: {
                    x: 1460,
                    y: 775,
                    text: "Torso\n(6,7,8)"
                },
                LL: {
                    x: 1130,
                    y: 1050,
                    text: "Left Leg\n(9)"
                },
                RL: {
                    x: 1795,
                    y: 1050,
                    text: "Right Leg\n(5)"
                },
                TR: {
                    x: 1460,
                    y: 1375,
                    text: "Torso Rear"
                }
            },
            pips: {
                HD: {
                    armor: {
                        start: {
                            x: 1610,
                            y: 330
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }],
                        mask: e => e % 2 !== 0
                    },
                    structure: {
                        start: {
                            x: 1610,
                            y: 415
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }]
                    }
                },
                LA: {
                    armor: {
                        start: {
                            x: 1320,
                            y: 530
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .175,
                            y: -1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.35,
                            y: 2
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .525,
                            y: -3
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.7,
                            y: 4
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 1.875,
                            y: -5
                        }]
                    },
                    structure: {
                        start: {
                            x: 1287,
                            y: 698
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -.175,
                            y: 1
                        }, {
                            x: .35,
                            y: -2
                        }, {
                            x: -.525,
                            y: 3
                        }, {
                            x: .7,
                            y: -4
                        }, {
                            x: -.875,
                            y: 5
                        }]
                    }
                },
                RA: {
                    armor: {
                        start: {
                            x: 1900,
                            y: 530
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.175,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .35,
                            y: 2
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.525,
                            y: -3
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .7,
                            y: 4
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -1.875,
                            y: -5
                        }]
                    },
                    structure: {
                        start: {
                            x: 1933,
                            y: 698
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: .175,
                            y: 1
                        }, {
                            x: -.35,
                            y: -2
                        }, {
                            x: .525,
                            y: 3
                        }, {
                            x: -.7,
                            y: -4
                        }, {
                            x: .875,
                            y: 5
                        }]
                    }
                },
                T: {
                    armor: {
                        start: {
                            x: 1610,
                            y: 540
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -1,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -3,
                            y: -1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -5,
                            y: 1
                        }, {
                            x: 6,
                            y: 0
                        }, {
                            x: -7,
                            y: -1
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -9,
                            y: 1
                        }, {
                            x: 10,
                            y: 0
                        }, {
                            x: -11,
                            y: -1
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -13,
                            y: 1
                        }, {
                            x: 14,
                            y: 0
                        }, {
                            x: -15,
                            y: -1
                        }, {
                            x: 16,
                            y: 0
                        }, {
                            x: -14,
                            y: -1
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -14,
                            y: 0
                        }, {
                            x: 16,
                            y: 0
                        }],
                        mask: e => e % 2 === 0
                    },
                    structure: {
                        start: {
                            x: 1610,
                            y: 640
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -4,
                            y: -1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -3,
                            y: 2
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -2,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }],
                        mask: e => e % 2 !== 0
                    }
                },
                LL: {
                    armor: {
                        start: {
                            x: 1470,
                            y: 1020
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .407,
                            y: -1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.814,
                            y: 2
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 1.221,
                            y: -3
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -1.628,
                            y: 4
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 2.035,
                            y: -5
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -2.442,
                            y: 6
                        }, {
                            x: -2,
                            y: 0
                        }]
                    },
                    structure: {
                        start: {
                            x: 1396,
                            y: 1246
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: .407,
                            y: -1
                        }, {
                            x: -.814,
                            y: 2
                        }, {
                            x: 1.221,
                            y: -3
                        }, {
                            x: -1.628,
                            y: 4
                        }, {
                            x: 2.035,
                            y: -5
                        }, {
                            x: -2.442,
                            y: 6
                        }]
                    }
                },
                RL: {
                    armor: {
                        start: {
                            x: 1750,
                            y: 1020
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.407,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .814,
                            y: 2
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -1.221,
                            y: -3
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 1.628,
                            y: 4
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -2.035,
                            y: -5
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 2.442,
                            y: 6
                        }, {
                            x: 2,
                            y: 0
                        }]
                    },
                    structure: {
                        start: {
                            x: 1824,
                            y: 1246
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -.407,
                            y: -1
                        }, {
                            x: .814,
                            y: 2
                        }, {
                            x: -1.221,
                            y: -3
                        }, {
                            x: 1.628,
                            y: 4
                        }, {
                            x: -2.035,
                            y: -5
                        }, {
                            x: 2.442,
                            y: 6
                        }]
                    }
                },
                TR: {
                    armor: {
                        start: {
                            x: 1610,
                            y: 1215
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -4,
                            y: -1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -3,
                            y: 2
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -2,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }],
                        mask: e => e % 2 !== 0
                    }
                }
            }
        })
          , Aa = {
            labels: {
                HD: {
                    x: 1500,
                    y: 235,
                    text: "Head (12)"
                },
                LFL: {
                    x: 1200,
                    y: 1340,
                    text: "Left\nFront Leg\n(10,11)"
                },
                RFL: {
                    x: 1800,
                    y: 1340,
                    text: "Right\nFront Leg\n(3,4)"
                },
                T: {
                    x: 1295,
                    y: 415,
                    text: "Torso\n(6,7,8)"
                },
                LRL: {
                    x: 1400,
                    y: 1300,
                    text: "Left\nRear Leg\n(9)"
                },
                RRL: {
                    x: 1600,
                    y: 1300,
                    text: "Right\nRear Leg\n(5)"
                },
                TR: {
                    x: 1093,
                    y: 775,
                    text: "Torso Rear"
                }
            },
            pips: {
                HD: {
                    armor: {
                        start: {
                            x: 1648,
                            y: 344
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }],
                        mask: e => e % 2 !== 0
                    },
                    structure: {
                        start: {
                            x: 1648,
                            y: 433
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }]
                    }
                },
                T: {
                    armor: {
                        start: {
                            x: 1647,
                            y: 555
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -1,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -3,
                            y: -1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -5,
                            y: 1
                        }, {
                            x: 6,
                            y: 0
                        }, {
                            x: -7,
                            y: -1
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -9,
                            y: 1
                        }, {
                            x: 10,
                            y: 0
                        }, {
                            x: -11,
                            y: -1
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -13,
                            y: 1
                        }, {
                            x: 14,
                            y: 0
                        }, {
                            x: -15,
                            y: -1
                        }, {
                            x: 16,
                            y: 0
                        }, {
                            x: -17,
                            y: -1
                        }, {
                            x: 18,
                            y: 0
                        }, {
                            x: -19,
                            y: 1
                        }, {
                            x: 20,
                            y: 0
                        }],
                        mask: e => e % 2 === 0
                    },
                    structure: {
                        start: {
                            x: 1647,
                            y: 648
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -4,
                            y: -1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -3,
                            y: 2
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -2,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }],
                        mask: e => e % 2 !== 0
                    }
                },
                LFL: {
                    armor: {
                        start: {
                            x: 1417,
                            y: 905
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .05,
                            y: -1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.1,
                            y: 2
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .15,
                            y: -3
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.2,
                            y: 4
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .25,
                            y: -5
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.3,
                            y: 6
                        }, {
                            x: -2,
                            y: 0
                        }]
                    },
                    structure: {
                        start: {
                            x: 1382,
                            y: 1130
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: .05,
                            y: -1
                        }, {
                            x: -.1,
                            y: 2
                        }, {
                            x: .15,
                            y: -3
                        }, {
                            x: -.2,
                            y: 4
                        }, {
                            x: .25,
                            y: -5
                        }, {
                            x: -.3,
                            y: 6
                        }]
                    }
                },
                LRL: {
                    armor: {
                        start: {
                            x: 1560,
                            y: 910
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .05,
                            y: -1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.1,
                            y: 2
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .15,
                            y: -3
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.2,
                            y: 4
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .25,
                            y: -5
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.3,
                            y: 6
                        }, {
                            x: -2,
                            y: 0
                        }]
                    },
                    structure: {
                        start: {
                            x: 1535,
                            y: 1130
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: .05,
                            y: -1
                        }, {
                            x: -.1,
                            y: 2
                        }, {
                            x: .15,
                            y: -3
                        }, {
                            x: -.2,
                            y: 4
                        }, {
                            x: .25,
                            y: -5
                        }, {
                            x: -.3,
                            y: 6
                        }]
                    }
                },
                RRL: {
                    armor: {
                        start: {
                            x: 1738,
                            y: 910
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.05,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .1,
                            y: 2
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.15,
                            y: -3
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .2,
                            y: 4
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.25,
                            y: -5
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .3,
                            y: 6
                        }, {
                            x: 2,
                            y: 0
                        }]
                    },
                    structure: {
                        start: {
                            x: 1761,
                            y: 1130
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -.05,
                            y: -1
                        }, {
                            x: .1,
                            y: 2
                        }, {
                            x: -.15,
                            y: -3
                        }, {
                            x: .2,
                            y: 4
                        }, {
                            x: -.25,
                            y: -5
                        }, {
                            x: .3,
                            y: 6
                        }]
                    }
                },
                RFL: {
                    armor: {
                        start: {
                            x: 1879,
                            y: 905
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.05,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .1,
                            y: 2
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.15,
                            y: -3
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .2,
                            y: 4
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -.25,
                            y: -5
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: .3,
                            y: 6
                        }, {
                            x: 2,
                            y: 0
                        }]
                    },
                    structure: {
                        start: {
                            x: 1919,
                            y: 1130
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -.05,
                            y: -1
                        }, {
                            x: .1,
                            y: 2
                        }, {
                            x: -.15,
                            y: -3
                        }, {
                            x: .2,
                            y: 4
                        }, {
                            x: -.25,
                            y: -5
                        }, {
                            x: .3,
                            y: 6
                        }]
                    }
                },
                TR: {
                    armor: {
                        start: {
                            x: 1245,
                            y: 615
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -4,
                            y: -1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -3,
                            y: 2
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -2,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }],
                        mask: e => e % 2 !== 0
                    }
                }
            }
        }
          , Ma = {
            labels: {
                FR: {
                    x: 1460,
                    y: 240,
                    text: "Front\n(6,7,8)"
                },
                LS: {
                    x: 1065,
                    y: 800,
                    text: "Left Side\n(9,10,11)"
                },
                RS: {
                    x: 1855,
                    y: 800,
                    text: "Right Side\n(3,4,5)"
                },
                RR: {
                    x: 1460,
                    y: 1400,
                    text: "Rear"
                }
            },
            pips: {
                FR: {
                    armor: {
                        start: {
                            x: 1610,
                            y: 530
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -4,
                            y: 1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -6,
                            y: -1
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -8,
                            y: 1
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -10,
                            y: -1
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -12,
                            y: 1
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -14,
                            y: -1
                        }, {
                            x: 16,
                            y: 0
                        }, {
                            x: -8,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -6,
                            y: 0
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -10,
                            y: 0
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -14,
                            y: 0
                        }, {
                            x: 16,
                            y: 0
                        }, {
                            x: -10,
                            y: -1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }],
                        mask: e => e < 17 ? e % 2 !== 0 : e % 2 === 0
                    },
                    structure: {
                        start: {
                            x: 1610,
                            y: 607
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }],
                        mask: e => e % 2 === 0
                    }
                },
                LS: {
                    armor: {
                        start: {
                            x: 1450,
                            y: 710
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: .2,
                            y: -1
                        }, {
                            x: -.4,
                            y: 2
                        }, {
                            x: .6,
                            y: -3
                        }, {
                            x: -.8,
                            y: 4
                        }, {
                            x: -1.6,
                            y: -2
                        }, {
                            x: .2,
                            y: -1
                        }, {
                            x: -.4,
                            y: 2
                        }, {
                            x: .6,
                            y: -3
                        }, {
                            x: -.8,
                            y: 4
                        }, {
                            x: 1,
                            y: -5
                        }, {
                            x: -1.2,
                            y: 6
                        }, {
                            x: 1.4,
                            y: -7
                        }, {
                            x: -2.8,
                            y: 4
                        }, {
                            x: .2,
                            y: -1
                        }, {
                            x: -.4,
                            y: 2
                        }, {
                            x: .6,
                            y: -3
                        }, {
                            x: -.8,
                            y: 4
                        }, {
                            x: 1,
                            y: -5
                        }, {
                            x: -1.2,
                            y: 6
                        }, {
                            x: 1.4,
                            y: -7
                        }, {
                            x: -1.6,
                            y: 8
                        }, {
                            x: 1.8,
                            y: -9
                        }]
                    },
                    structure: {
                        start: {
                            x: 1422,
                            y: 918
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: .35,
                            y: -1
                        }, {
                            x: -.7,
                            y: 2
                        }],
                        mask: e => e % 2 === 0
                    }
                },
                RS: {
                    armor: {
                        start: {
                            x: 1770,
                            y: 710
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -.2,
                            y: -1
                        }, {
                            x: .4,
                            y: 2
                        }, {
                            x: -.6,
                            y: -3
                        }, {
                            x: .8,
                            y: 4
                        }, {
                            x: 1.6,
                            y: -2
                        }, {
                            x: -.2,
                            y: -1
                        }, {
                            x: .4,
                            y: 2
                        }, {
                            x: -.6,
                            y: -3
                        }, {
                            x: .8,
                            y: 4
                        }, {
                            x: -1,
                            y: -5
                        }, {
                            x: 1.2,
                            y: 6
                        }, {
                            x: -1.4,
                            y: -7
                        }, {
                            x: 2.8,
                            y: 4
                        }, {
                            x: -.2,
                            y: -1
                        }, {
                            x: .4,
                            y: 2
                        }, {
                            x: -.6,
                            y: -3
                        }, {
                            x: .8,
                            y: 4
                        }, {
                            x: -1,
                            y: -5
                        }, {
                            x: 1.2,
                            y: 6
                        }, {
                            x: -1.4,
                            y: -7
                        }, {
                            x: 1.6,
                            y: 8
                        }, {
                            x: -1.8,
                            y: -9
                        }]
                    },
                    structure: {
                        start: {
                            x: 1798,
                            y: 918
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -.35,
                            y: -1
                        }, {
                            x: .7,
                            y: 2
                        }],
                        mask: e => e % 2 === 0
                    }
                },
                RR: {
                    armor: {
                        start: {
                            x: 1610,
                            y: 1295
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -6,
                            y: 0
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -10,
                            y: 0
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -12,
                            y: -1
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -14,
                            y: 0
                        }, {
                            x: 16,
                            y: 0
                        }, {
                            x: -18,
                            y: 0
                        }, {
                            x: 20,
                            y: 0
                        }, {
                            x: -16,
                            y: -1
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -14,
                            y: 0
                        }, {
                            x: 16,
                            y: 0
                        }],
                        mask: e => e % 2 === 0
                    },
                    structure: {
                        start: {
                            x: 1610,
                            y: 1225
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }],
                        mask: e => e % 2 === 0
                    }
                }
            },
            turret: {
                labels: {
                    FR: {
                        x: 1460,
                        y: 240,
                        text: "Front\n(6,7,8)"
                    },
                    TU: {
                        x: 1460,
                        y: 1137,
                        text: "Turret (5,9)"
                    },
                    LS: {
                        x: 1065,
                        y: 800,
                        text: "Left Side\n(10,11)"
                    },
                    RS: {
                        x: 1855,
                        y: 800,
                        text: "Right Side\n(3,4)"
                    },
                    RR: {
                        x: 1460,
                        y: 1400,
                        text: "Rear"
                    }
                },
                pips: {
                    TU: {
                        armor: {
                            start: {
                                x: 1610,
                                y: 860
                            },
                            steps: [{
                                x: 0,
                                y: 0
                            }, {
                                x: 0,
                                y: 1
                            }, {
                                x: -2,
                                y: 0
                            }, {
                                x: 4,
                                y: 0
                            }, {
                                x: -3,
                                y: 1
                            }, {
                                x: 2,
                                y: 0
                            }, {
                                x: -4,
                                y: 0
                            }, {
                                x: 6,
                                y: 0
                            }, {
                                x: -4,
                                y: 1
                            }, {
                                x: 2,
                                y: 0
                            }, {
                                x: -4,
                                y: 0
                            }, {
                                x: 6,
                                y: 0
                            }, {
                                x: -4,
                                y: 1
                            }, {
                                x: 2,
                                y: 0
                            }, {
                                x: -4,
                                y: 0
                            }, {
                                x: 6,
                                y: 0
                            }, {
                                x: -4,
                                y: 1
                            }, {
                                x: 2,
                                y: 0
                            }, {
                                x: -4,
                                y: 0
                            }, {
                                x: 6,
                                y: 0
                            }],
                            mask: e => e % 2 !== 0
                        },
                        structure: {
                            start: {
                                x: 1610,
                                y: 1060
                            },
                            steps: [{
                                x: 0,
                                y: 0
                            }, {
                                x: -2,
                                y: 0
                            }, {
                                x: 4,
                                y: 0
                            }],
                            mask: e => e % 2 === 0
                        }
                    }
                }
            }
        }
          , La = {
            labels: {
                FR: {
                    x: 1460,
                    y: 275,
                    text: "Front (6,7,8)"
                },
                LS: {
                    x: 1240,
                    y: 500,
                    text: "Left\nSide\n(10,11)"
                },
                RS: {
                    x: 1680,
                    y: 500,
                    text: "Right\nSide\n(3,4)"
                },
                RR: {
                    x: 1350,
                    y: 1120,
                    text: "Rear"
                },
                RO: {
                    x: 1150,
                    y: 780,
                    text: "Rotor\n(5,9)"
                }
            },
            pips: {
                FR: {
                    armor: {
                        start: {
                            x: 1609,
                            y: 430
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -4,
                            y: 1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -6,
                            y: 0
                        }, {
                            x: 8,
                            y: 0
                        }],
                        mask: e => e % 2 !== 0
                    },
                    structure: {
                        start: {
                            x: 1609,
                            y: 500
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }]
                    }
                },
                LS: {
                    armor: {
                        start: {
                            x: 1519,
                            y: 590
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: -1
                        }, {
                            x: 0,
                            y: 2
                        }, {
                            x: 0,
                            y: -3
                        }, {
                            x: 0,
                            y: 4
                        }]
                    },
                    structure: {
                        start: {
                            x: 1531,
                            y: 800
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }]
                    }
                },
                RS: {
                    armor: {
                        start: {
                            x: 1699,
                            y: 590
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: -1
                        }, {
                            x: 0,
                            y: 2
                        }, {
                            x: 0,
                            y: -3
                        }, {
                            x: 0,
                            y: 4
                        }]
                    },
                    structure: {
                        start: {
                            x: 1687,
                            y: 800
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }]
                    }
                },
                RR: {
                    armor: {
                        start: {
                            x: 1613,
                            y: 1130
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }]
                    },
                    structure: {
                        start: {
                            x: 1613,
                            y: 1060
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }]
                    }
                },
                RO: {
                    armor: {
                        start: {
                            x: 1609,
                            y: 698
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }]
                    },
                    structure: {
                        start: {
                            x: 1609,
                            y: 740
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }]
                    }
                }
            }
        }
          , fa = {
            labels: {
                N: {
                    x: 1300,
                    y: 300,
                    text: "Nose\n(6,7,8)"
                },
                LW: {
                    x: 1200,
                    y: 770,
                    text: "Left\nWing\n(9,10,11)"
                },
                RW: {
                    x: 1725,
                    y: 770,
                    text: "Right\nWing\n(3,4,5)"
                },
                A: {
                    x: 1460,
                    y: 1350,
                    text: "Aft\n(2,12)"
                }
            },
            pips: {
                FU: {
                    structure: {
                        start: {
                            x: 1610,
                            y: 800
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }]
                    }
                },
                N: {
                    armor: {
                        start: {
                            x: 1610,
                            y: 575
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -4,
                            y: 1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -6,
                            y: -1
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -8,
                            y: 1
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -10,
                            y: -1
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -12,
                            y: 1
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -14,
                            y: -1
                        }, {
                            x: 16,
                            y: 0
                        }, {
                            x: -8,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -6,
                            y: 0
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -10,
                            y: 0
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -14,
                            y: 0
                        }, {
                            x: 16,
                            y: 0
                        }, {
                            x: -10,
                            y: -1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }],
                        mask: e => e < 17 ? e % 2 !== 0 : e % 2 === 0
                    }
                },
                LW: {
                    armor: {
                        start: {
                            x: 1500,
                            y: 1030
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: -1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 4,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 6,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 7,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 11,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: 11,
                            y: 1
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }, {
                            x: -2,
                            y: 0
                        }]
                    }
                },
                RW: {
                    armor: {
                        start: {
                            x: 1711,
                            y: 1030
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: -1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -4,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -6,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -7,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -11,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: -11,
                            y: 1
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }, {
                            x: 2,
                            y: 0
                        }]
                    }
                },
                A: {
                    armor: {
                        start: {
                            x: 1610,
                            y: 1130
                        },
                        steps: [{
                            x: 0,
                            y: 0
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: 0,
                            y: 1
                        }, {
                            x: -2,
                            y: -4
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -4,
                            y: 1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -6,
                            y: 0
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -6,
                            y: 1
                        }, {
                            x: 4,
                            y: 0
                        }, {
                            x: -6,
                            y: 0
                        }, {
                            x: 8,
                            y: 0
                        }, {
                            x: -10,
                            y: 0
                        }, {
                            x: 12,
                            y: 0
                        }, {
                            x: -4,
                            y: 1
                        }, {
                            x: -4,
                            y: 0
                        }, {
                            x: 6,
                            y: 0
                        }, {
                            x: -8,
                            y: 0
                        }, {
                            x: 10,
                            y: 0
                        }, {
                            x: -12,
                            y: 0
                        }, {
                            x: 8,
                            y: 1
                        }, {
                            x: -4,
                            y: 0
                        }, {
                            x: 6,
                            y: 0
                        }, {
                            x: -8,
                            y: 0
                        }, {
                            x: 10,
                            y: 0
                        }, {
                            x: -12,
                            y: 0
                        }]
                    }
                }
            }
        }
          , Sa = e => {
            let {type: a, motive: t, hasTurret: n} = e;
            const s = t === X.MotiveTypeEnum.T
              , r = t === X.MotiveTypeEnum.W;
            var i = (0,
            b.jsx)(Ca, {
                imageURL: ( (e, a) => {
                    switch (e) {
                    case A.UnitTypeEnum.BM:
                        return a === L.MotiveTypeEnum.BP ? pe : ye;
                    case A.UnitTypeEnum.CV:
                        return a === X.MotiveTypeEnum.V ? Le : xe;
                    case A.UnitTypeEnum.AF:
                        return fe;
                    default:
                        return null
                    }
                }
                )(a, t)
            });
            return (0,
            b.jsxs)(ue.Group, {
                children: [s ? (0,
                b.jsx)(Ca, {
                    imageURL: Ae
                }) : null, r ? (0,
                b.jsx)(Ca, {
                    imageURL: Me
                }) : null, i, n ? (0,
                b.jsx)(Ca, {
                    imageURL: ve
                }) : null]
            })
        }
          , ba = e => {
            let {rank: a} = e;
            var t;
            if (1 === a)
                t = Se;
            else if (2 === a)
                t = be;
            else if (3 === a)
                t = Ce;
            else if (4 === a)
                t = Te;
            else {
                if (5 !== a)
                    return null;
                t = Re
            }
            return (0,
            b.jsx)(Ca, {
                imageURL: t,
                x: xa.x,
                y: xa.y
            })
        }
          , Ca = e => {
            let {imageURL: a, width: t, height: n, x: s, y: r} = e;
            const [i] = ce()(a);
            return (0,
            b.jsx)(ue.Image, {
                image: i,
                width: t,
                height: n,
                x: s,
                y: r
            })
        }
        ;
        class Ta extends n.Component {
            constructor(e) {
                super(e),
                this.getDestiny = () => null != localStorage.getItem("destiny") && localStorage.getItem("destiny").includes('"isDestinyEnabled":true'),
                this.getDestinyInverse = () => 1 != this.getDestiny(),
                this.container = null,
                this.setContainerRef = e => {
                    this.container = e
                }
                ,
                this.fileInput = n.createRef(),
                this.handleResize = this.handleResize.bind(this),
                this.handleUnitFileChange = this.handleUnitFileChange.bind(this),
                this.onBackgroundConfigChange = this.onBackgroundConfigChange.bind(this),
                this.showBackgroundModal = this.showBackgroundModal.bind(this),
                this.onCloseBackgroundModal = this.onCloseBackgroundModal.bind(this),
                this.state = {
                    file: null,
                    unitImage: null,
                    scale: 1,
                    opacity: .18,
                    imgX: 0,
                    imgY: 0,
                    showBackgroundModal: !1
                }
            }
            render() {
                var e;
                return (0,
                b.jsxs)("div", {
                    className: "card-body mt-0 pt-0",
                    children: [(0,
                    b.jsx)("div", {
                        ref: this.setContainerRef,
                        children: (0,
                        b.jsx)(ue.Stage, {
                            ref: this.props.stageRef,
                            width: this.props.width,
                            height: this.props.height,
                            children: (0,
                            b.jsx)(ue.Layer, {
                                listening: !1,
                                preventDefault: !1,
                                children: (0,
                                b.jsxs)(ue.Group, {
                                    children: [(0,
                                    b.jsx)(Ca, {
                                        imageURL: ge
                                    }), (0,
                                    b.jsx)(ue.Image, {
                                        image: this.state.unitImage,
                                        x: this.state.imgX,
                                        y: this.state.imgY,
                                        scaleX: this.state.scale,
                                        scaleY: this.state.scale,
                                        opacity: this.state.opacity
                                    }), (0,
                                    b.jsx)(Sa, {
                                        type: this.props.data.unitType,
                                        motive: this.props.data.motiveType,
                                        hasTurret: this.props.data.hasTurret
                                    }), null !== (e = this.props.data) && void 0 !== e && e.pilotBlank ? null : (0,
                                    b.jsx)(ba, {
                                        rank: this.props.data.skillsRank
                                    })]
                                })
                            })
                        })
                    }), (0,
                    b.jsx)(i.A, {
                        onClick: this.showBackgroundModal,
                        className: "mt-1 mb-2",
                        style: {
                            marginLeft: -4
                        },
                        disabled: this.getDestinyInverse(),
                        children: "Set Card Background"
                    }), (0,
                    b.jsxs)(oe.A, {
                        show: this.state.showBackgroundModal,
                        onHide: this.onCloseBackgroundModal,
                        backdrop: "static",
                        centered: !0,
                        children: [(0,
                        b.jsxs)(oe.A.Header, {
                            className: "bg-gray-dark border-0",
                            children: ["Select, Scale, and Place a Background Image for this Card", (0,
                            b.jsx)(i.A, {
                                onClick: this.onCloseBackgroundModal,
                                size: "sm",
                                children: (0,
                                b.jsx)(S.hvQ, {})
                            })]
                        }), (0,
                        b.jsx)(oe.A.Body, {
                            className: "bg-gray-dark border-0",
                            children: (0,
                            b.jsxs)(r.A, {
                                children: [(0,
                                b.jsx)(r.A.Group, {
                                    children: (0,
                                    b.jsxs)(r.A.File, {
                                        id: "file",
                                        custom: !0,
                                        children: [(0,
                                        b.jsx)(r.A.File.Input, {
                                            ref: this.fileInput,
                                            accept: ".png",
                                            onChange: this.handleUnitFileChange
                                        }), (0,
                                        b.jsx)(r.A.File.Label, {
                                            children: this.state.file ? this.state.file : "Choose file"
                                        })]
                                    })
                                }), (0,
                                b.jsxs)(r.A.Row, {
                                    children: [(0,
                                    b.jsxs)(r.A.Group, {
                                        as: s.A,
                                        controlId: "imgX",
                                        children: [(0,
                                        b.jsx)(r.A.Label, {
                                            children: "X"
                                        }), (0,
                                        b.jsx)("br", {}), (0,
                                        b.jsx)(r.A.Control, {
                                            type: "number",
                                            value: this.state.imgX,
                                            size: "sm",
                                            onChange: this.onBackgroundConfigChange,
                                            custom: !0
                                        })]
                                    }), (0,
                                    b.jsxs)(r.A.Group, {
                                        as: s.A,
                                        controlId: "imgY",
                                        children: [(0,
                                        b.jsx)(r.A.Label, {
                                            children: "Y"
                                        }), (0,
                                        b.jsx)("br", {}), (0,
                                        b.jsx)(r.A.Control, {
                                            type: "number",
                                            value: this.state.imgY,
                                            size: "sm",
                                            onChange: this.onBackgroundConfigChange,
                                            custom: !0
                                        })]
                                    })]
                                }), (0,
                                b.jsxs)(r.A.Row, {
                                    children: [(0,
                                    b.jsxs)(r.A.Group, {
                                        as: s.A,
                                        controlId: "scale",
                                        children: [(0,
                                        b.jsx)(r.A.Label, {
                                            children: "Scale"
                                        }), (0,
                                        b.jsx)("br", {}), (0,
                                        b.jsx)(r.A.Control, {
                                            type: "number",
                                            step: .01,
                                            precision: 2,
                                            min: .01,
                                            value: this.state.scale,
                                            size: "sm",
                                            onChange: this.onBackgroundConfigChange,
                                            custom: !0
                                        })]
                                    }), (0,
                                    b.jsxs)(r.A.Group, {
                                        as: s.A,
                                        controlId: "opacity",
                                        children: [(0,
                                        b.jsx)(r.A.Label, {
                                            children: "Opacity"
                                        }), (0,
                                        b.jsx)("br", {}), (0,
                                        b.jsx)(r.A.Control, {
                                            type: "number",
                                            step: .01,
                                            precision: 2,
                                            min: 0,
                                            max: 1,
                                            value: this.state.opacity,
                                            size: "sm",
                                            onChange: this.onBackgroundConfigChange,
                                            custom: !0
                                        })]
                                    })]
                                })]
                            })
                        })]
                    })]
                })
            }
            handleUnitFileChange(e) {
                let a = e.target.files[0]
                  , t = new FileReader;
                t.addEventListener("load", e => {
                    let t = new Image;
                    t.src = e.target.result,
                    t.onload = () => {
                        this.setState({
                            unitImage: t,
                            file: a.name
                        })
                    }
                }
                ),
                t.readAsDataURL(a)
            }
            showBackgroundModal(e) {
                this.setState({
                    showBackgroundModal: !0
                })
            }
            onBackgroundConfigChange(e) {
                if (e && e.currentTarget) {
                    let a = e.currentTarget
                      , t = a.id
                      , n = +a.value
                      , s = {};
                    s[t] = n,
                    this.setState(s)
                }
            }
            onCloseBackgroundModal(e) {
                this.setState({
                    showBackgroundModal: !1
                })
            }
            componentDidMount() {
                this.handleResize(),
                window.addEventListener("resize", this.handleResize),
                this.renderData(this.props.data)
            }
            componentWillUnmount() {
                window.removeEventListener("resize", this.handleResize)
            }
            componentDidUpdate(e) {
                this.renderData(this.props.data)
            }
            handleResize() {
                if (!this.props.stageRef)
                    return;
                const e = this.props.stageRef.current;
                if (!this.container || !e)
                    return;
                const a = this.container.offsetWidth
                  , t = a / this.props.width
                  , n = Math.round(this.props.height * t);
                e.size({
                    width: a,
                    height: n
                }),
                e.scale({
                    x: t,
                    y: t
                })
            }
            renderData(e) {
                if (!this.props.stageRef)
                    return;
                const a = this.props.stageRef.current;
                if (!a)
                    return;
                const t = a.children[0];
                if (!t)
                    return;
                const n = t.children[1];
                n && n.destroy();
                const s = new (de().Group);
                e.unitBlank || s.add(new (de().Text)({
                    x: Be.x,
                    y: Be.y,
                    text: e.unitName,
                    fontSize: 66,
                    fontFamily: "vegas-regular",
                    width: 1060,
                    wrap: "none"
                })),
                s.add(new (de().Text)({
                    x: Pe.x,
                    y: Pe.y,
                    text: "UNIT DATA",
                    fontSize: 44,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: ke.x,
                    y: ke.y,
                    text: "Type:",
                    fontSize: je,
                    fontFamily: "falcon-bold"
                })),
                e.unitBlank || s.add(new (de().Text)({
                    x: Ie.x,
                    y: Ie.y,
                    text: e.unitTypeName,
                    fontSize: je,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Text)({
                    x: Fe.x,
                    y: Fe.y,
                    text: "Mass:",
                    fontSize: je,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: qe.x,
                    y: qe.y,
                    text: e.unitBlank ? "       Tons" : e.mass + " Tons",
                    fontSize: je,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Text)({
                    x: Xe.x,
                    y: Xe.y,
                    text: e.unitType === A.UnitTypeEnum.AF ? "Thrust:" : "Move:",
                    fontSize: je,
                    fontFamily: "falcon-bold"
                })),
                e.unitBlank || s.add(new (de().Text)({
                    x: Ne.x + (e.unitType === A.UnitTypeEnum.AF ? 15 : 0),
                    y: Ne.y,
                    text: e.move,
                    fontSize: je,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Text)({
                    x: We.x,
                    y: We.y,
                    text: "TMM:",
                    fontSize: je,
                    fontFamily: "falcon-bold"
                })),
                e.unitBlank || s.add(new (de().Text)({
                    x: ze.x + (e.unitType === A.UnitTypeEnum.AF ? 15 : 0),
                    y: ze.y,
                    text: e.tmm,
                    fontSize: je,
                    fontFamily: "falcon-regular"
                })),
                e.unitType === A.UnitTypeEnum.AF && (s.add(new (de().Text)({
                    x: Ge.x,
                    y: We.y,
                    text: "DThr:",
                    fontSize: je,
                    fontFamily: "falcon-bold"
                })),
                e.unitBlank || s.add(new (de().Text)({
                    x: Oe.x,
                    y: ze.y,
                    text: e.damageThreshold,
                    fontSize: je,
                    fontFamily: "falcon-regular"
                }))),
                e.hasHeat && (s.add(new (de().Text)({
                    x: Ge.x,
                    y: Ge.y,
                    text: "Sinks:",
                    fontSize: je,
                    fontFamily: "falcon-bold"
                })),
                e.unitBlank || s.add(new (de().Text)({
                    x: Oe.x,
                    y: Oe.y,
                    text: e.sinks,
                    fontSize: je,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Text)({
                    x: De.x,
                    y: De.y,
                    text: "Heat Scale",
                    fontSize: je,
                    fontFamily: "falcon-regular",
                    rotation: 270
                })),
                s.add(new (de().Rect)({
                    x: Ue.x - 13,
                    y: Ue.y - 11,
                    height: 44,
                    width: 44,
                    stroke: "black",
                    strokeWidth: 4,
                    cornerRadius: 1,
                    fill: "#000000"
                })),
                s.add(new (de().Text)({
                    x: Ue.x,
                    y: Ue.y,
                    text: "5",
                    fontSize: we,
                    fontFamily: "falcon-bold",
                    fill: "#F0F0F0"
                })),
                s.add(new (de().Text)({
                    x: Ue.x + 50,
                    y: Ue.y,
                    text: "Automatic Shutdown",
                    fontSize: we,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Rect)({
                    x: He.x - 13,
                    y: He.y - 11,
                    height: 44,
                    width: 44,
                    stroke: "black",
                    strokeWidth: 4,
                    cornerRadius: 1,
                    fillLinearGradientStartPoint: {
                        x: 0,
                        y: 22
                    },
                    fillLinearGradientEndPoint: {
                        x: 0,
                        y: -22
                    },
                    fillLinearGradientColorStops: [0, "#FF6666", 1, "#000000"]
                })),
                s.add(new (de().Text)({
                    x: He.x,
                    y: He.y,
                    text: "4",
                    fontSize: we,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: He.x + 50,
                    y: He.y,
                    text: "Ammo Explosion (avoid 8+)",
                    fontSize: we,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Rect)({
                    x: Ve.x - 13,
                    y: Ve.y - 11,
                    height: 44,
                    width: 44,
                    stroke: "black",
                    strokeWidth: 4,
                    cornerRadius: 1,
                    fillLinearGradientStartPoint: {
                        x: 0,
                        y: 44
                    },
                    fillLinearGradientEndPoint: {
                        x: 0,
                        y: 0
                    },
                    fillLinearGradientColorStops: [0, "#FFB266", 1, "#FF6666"]
                })),
                s.add(new (de().Text)({
                    x: Ve.x,
                    y: Ve.y,
                    text: "3",
                    fontSize: we,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: Ve.x + 50,
                    y: Ve.y,
                    text: "Shutdown (avoid 8+)",
                    fontSize: we,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Rect)({
                    x: Je.x - 13,
                    y: Je.y - 11,
                    height: 44,
                    width: 44,
                    stroke: "black",
                    strokeWidth: 4,
                    cornerRadius: 1,
                    fillLinearGradientStartPoint: {
                        x: 0,
                        y: 44
                    },
                    fillLinearGradientEndPoint: {
                        x: 0,
                        y: 22
                    },
                    fillLinearGradientColorStops: [0, "#FFFF66", 1, "#FFB266"]
                })),
                s.add(new (de().Text)({
                    x: Je.x,
                    y: Je.y,
                    text: "2",
                    fontSize: we,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: Je.x + 50,
                    y: Je.y,
                    text: "+1 Ranged Attack Mod",
                    fontSize: we,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Rect)({
                    x: Qe.x - 13,
                    y: Qe.y - 11,
                    height: 44,
                    width: 44,
                    stroke: "black",
                    strokeWidth: 4,
                    cornerRadius: 1,
                    fillLinearGradientStartPoint: {
                        x: 0,
                        y: 44
                    },
                    fillLinearGradientEndPoint: {
                        x: 0,
                        y: 22
                    },
                    fillLinearGradientColorStops: [0, "#FFFFFF", 1, "#FFFF66"]
                })),
                s.add(new (de().Text)({
                    x: Qe.x,
                    y: Qe.y,
                    text: "1",
                    fontSize: we,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: Qe.x + 50,
                    y: Qe.y,
                    text: "-2 " + (e.unitType === A.UnitTypeEnum.AF ? "Safe Thrust" : "Ground Move") + " / -1 TMM",
                    fontSize: we,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Rect)({
                    x: _e.x - 13,
                    y: _e.y - 11,
                    height: 44,
                    width: 44,
                    stroke: "black",
                    strokeWidth: 4,
                    cornerRadius: 1,
                    fill: "#FFFFFF"
                })),
                s.add(new (de().Text)({
                    x: _e.x,
                    y: _e.y,
                    text: "0",
                    fontSize: we,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: _e.x + 50,
                    y: _e.y,
                    text: "No Effects",
                    fontSize: we,
                    fontFamily: "falcon-regular"
                }))),
                s.add(new (de().Text)({
                    x: Ke.x,
                    y: Ke.y,
                    text: "WEAPONS",
                    fontSize: 44,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: Ze.x,
                    y: Ye.y - ya,
                    text: "Dmg",
                    fontSize: je,
                    fontFamily: "falcon-regular",
                    width: 220,
                    align: "center",
                    height: 72,
                    verticalAlign: "middle"
                })),
                e.hasHeat && s.add(new (de().Text)({
                    x: ea.x,
                    y: Ye.y - ya,
                    text: "Ht",
                    fontSize: je,
                    fontFamily: "falcon-regular",
                    width: 50,
                    align: "center",
                    height: 72,
                    verticalAlign: "middle"
                })),
                s.add(new (de().Text)({
                    x: ta.x - (e.hasHeat ? 0 : 40),
                    y: Ye.y - ya,
                    text: "Loc",
                    fontSize: je,
                    fontFamily: "falcon-regular",
                    width: 140,
                    align: "center",
                    height: 72,
                    verticalAlign: "middle"
                })),
                s.add(new (de().Text)({
                    x: sa.x,
                    y: Ye.y - ya,
                    text: "PB",
                    fontSize: je,
                    fontFamily: "falcon-regular",
                    width: 50,
                    align: "center",
                    height: 72,
                    verticalAlign: "middle"
                })),
                s.add(new (de().Text)({
                    x: ia.x,
                    y: Ye.y - ya,
                    text: "S",
                    fontSize: je,
                    fontFamily: "falcon-regular",
                    width: 50,
                    align: "center",
                    height: 72,
                    verticalAlign: "middle"
                })),
                s.add(new (de().Text)({
                    x: oa.x,
                    y: Ye.y - ya,
                    text: "M",
                    fontSize: je,
                    fontFamily: "falcon-regular",
                    width: 50,
                    align: "center",
                    height: 72,
                    verticalAlign: "middle"
                })),
                s.add(new (de().Text)({
                    x: ca.x,
                    y: Ye.y - ya,
                    text: "L",
                    fontSize: je,
                    fontFamily: "falcon-regular",
                    width: 50,
                    align: "center",
                    height: 72,
                    verticalAlign: "middle"
                })),
                s.add(new (de().Text)({
                    x: ha.x,
                    y: Ye.y - ya,
                    text: "X",
                    fontSize: je,
                    fontFamily: "falcon-regular",
                    width: 50,
                    align: "center",
                    height: 72,
                    verticalAlign: "middle"
                })),
                e.weapons.forEach( (a, t) => {
                    if (!e.unitBlank || a.melee) {
                        const n = Ye.y + (a.melee ? 9 : t) * ya;
                        s.add(new (de().Text)({
                            x: Ye.x,
                            y: n,
                            text: a.name,
                            fontSize: we,
                            fontFamily: "falcon-regular",
                            width: 360,
                            height: 72,
                            verticalAlign: "middle"
                        })),
                        s.add(new (de().Text)({
                            x: $e.x,
                            y: n,
                            text: a.damage,
                            fontSize: we,
                            fontFamily: "falcon-regular",
                            width: 220,
                            align: "center",
                            height: 72,
                            verticalAlign: "middle"
                        })),
                        e.hasHeat && s.add(new (de().Text)({
                            x: aa.x,
                            y: n,
                            text: a.heat,
                            fontSize: we,
                            fontFamily: "falcon-regular",
                            width: 50,
                            align: "center",
                            height: 72,
                            verticalAlign: "middle"
                        })),
                        s.add(new (de().Text)({
                            x: na.x - (e.hasHeat ? 0 : 40),
                            y: n,
                            text: a.location,
                            fontSize: we,
                            fontFamily: "falcon-regular",
                            width: 140,
                            align: "center",
                            height: 72,
                            verticalAlign: "middle"
                        })),
                        s.add(new (de().Text)({
                            x: ra.x,
                            y: n,
                            text: a.rangePB,
                            fontSize: we,
                            fontFamily: "falcon-regular",
                            width: 50,
                            align: "center",
                            height: 72,
                            verticalAlign: "middle"
                        })),
                        s.add(new (de().Text)({
                            x: la.x,
                            y: n,
                            text: a.rangeS,
                            fontSize: we,
                            fontFamily: "falcon-regular",
                            width: 50,
                            align: "center",
                            height: 72,
                            verticalAlign: "middle"
                        })),
                        s.add(new (de().Text)({
                            x: ma.x,
                            y: n,
                            text: a.rangeM,
                            fontSize: we,
                            fontFamily: "falcon-regular",
                            width: 50,
                            align: "center",
                            height: 72,
                            verticalAlign: "middle"
                        })),
                        s.add(new (de().Text)({
                            x: ua.x,
                            y: n,
                            text: a.rangeL,
                            fontSize: we,
                            fontFamily: "falcon-regular",
                            width: 50,
                            align: "center",
                            height: 72,
                            verticalAlign: "middle"
                        })),
                        s.add(new (de().Text)({
                            x: da.x,
                            y: n,
                            text: a.rangeX,
                            fontSize: we,
                            fontFamily: "falcon-regular",
                            width: 50,
                            align: "center",
                            height: 72,
                            verticalAlign: "middle"
                        }))
                    }
                }
                ),
                s.add(new (de().Text)({
                    x: ga.x,
                    y: ga.y,
                    text: "Equipment:",
                    fontSize: 32,
                    fontFamily: "falcon-bold",
                    verticalAlign: "top",
                    lineHeight: 1.1
                })),
                e.unitBlank || s.add(new (de().Text)({
                    x: pa.x,
                    y: pa.y,
                    text: e.equipment,
                    fontSize: 32,
                    fontFamily: "falcon-regular",
                    width: 880,
                    height: 120,
                    verticalAlign: "top",
                    lineHeight: 1.1
                })),
                s.add(new (de().Text)({
                    x: 1155,
                    y: 58,
                    text: "Gunnery",
                    fontSize: we,
                    fontFamily: "falcon-bold",
                    width: 180,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 1290,
                    y: 58,
                    text: "Piloting",
                    fontSize: we,
                    fontFamily: "falcon-bold",
                    width: 180,
                    align: "center"
                })),
                e.unitType === A.UnitTypeEnum.BM && (s.add(new (de().Text)({
                    x: 40,
                    y: 1338,
                    text: "Engine",
                    fontSize: we,
                    fontFamily: "falcon-bold",
                    width: 400,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 270,
                    y: 1338,
                    text: "Gyro",
                    fontSize: we,
                    fontFamily: "falcon-bold",
                    width: 400,
                    align: "center"
                }))),
                s.add(new (de().Text)({
                    x: 665,
                    y: 1338,
                    text: "Condition Monitor",
                    fontSize: we,
                    fontFamily: "falcon-bold",
                    width: 400,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 491,
                    y: 1384,
                    text: "3+",
                    fontSize: we,
                    fontFamily: "falcon",
                    width: 400,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 561,
                    y: 1384,
                    text: "5+",
                    fontSize: we,
                    fontFamily: "falcon",
                    width: 400,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 631,
                    y: 1384,
                    text: "7+",
                    fontSize: we,
                    fontFamily: "falcon",
                    width: 400,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 701,
                    y: 1384,
                    text: "9+",
                    fontSize: we,
                    fontFamily: "falcon",
                    width: 400,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 768,
                    y: 1384,
                    text: "11+",
                    fontSize: we,
                    fontFamily: "falcon",
                    width: 400,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 840,
                    y: 1384,
                    text: "KIA",
                    fontSize: we,
                    fontFamily: "falcon",
                    width: 400,
                    align: "center"
                }));
                var r, i = {}, l = 0;
                e.unitType === A.UnitTypeEnum.BM ? i = e.motiveType === L.MotiveTypeEnum.QD ? Aa : va : e.unitType === A.UnitTypeEnum.CV ? e.motiveType === X.MotiveTypeEnum.V ? i = La : (i = Ma,
                e.hasTurret && (r = Ma.turret)) : e.unitType === A.UnitTypeEnum.AF && (i = fa);
                var o = Object.assign({}, i.labels)
                  , m = Object.assign({}, i.pips);
                r && (Object.keys(r.labels).forEach(e => {
                    o[e] = r.labels[e]
                }
                ),
                Object.keys(r.pips).forEach(e => {
                    m[e] = r.pips[e]
                }
                )),
                Object.keys(o).forEach(e => {
                    s.add(new (de().Text)({
                        x: o[e].x,
                        y: o[e].y,
                        text: o[e].text,
                        fontSize: we,
                        fontFamily: "falcon-bold",
                        width: 300,
                        align: "center",
                        lineHeight: 1.1
                    }))
                }
                );
                const c = 7.5
                  , u = Ee * (Math.sqrt(3) / 2)
                  , h = Ee * Math.sqrt(3) + 1.5
                  , d = e.greenPips
                  , g = e.bluePips
                  , p = e.brownPips
                  , y = e.purplePips;
                let x = "black"
                  , v = "white"
                  , M = 3;
                d ? (x = "green",
                v = "rgba(0, 255, 0, 0.10)",
                M = 4) : g ? (x = "blue",
                v = "rgba(0, 255, 255, 0.15)",
                M = 4) : p ? (x = "rgba(127, 63, 0, 1.00)",
                v = "rgba(127, 63, 0, 0.15)",
                M = 4) : y ? (x = "rgba(41, 0, 85, 1.00)",
                v = "rgba(127, 0, 255, 0.10)",
                M = 4) : (x = "black",
                v = "white",
                M = 3),
                Object.keys(m).forEach(a => {
                    var t, n, r, i;
                    let o = m[a].armor
                      , d = e.unitBlank ? null === o || void 0 === o || null === (t = o.steps) || void 0 === t ? void 0 : t.length : null === (n = e.pips[a]) || void 0 === n ? void 0 : n.armor;
                    if (d && o) {
                        let a = o.mask
                          , t = o.steps.slice()
                          , n = o.start.x
                          , r = o.start.y;
                        for (a && d < t.length && a(d) && t.shift(),
                        l = 0; l < d && l < t.length; l++)
                            n += Math.round(16.5 * t[l].x),
                            r += Math.round(t[l].y * h),
                            s.add(new (de().RegularPolygon)({
                                x: n,
                                y: r,
                                radius: Ee,
                                sides: 6,
                                rotation: 30,
                                strokeWidth: M,
                                stroke: x,
                                fill: v
                            })),
                            e.sliceArmorPips && s.add(new (de().Line)({
                                points: [Math.round(n - c), Math.round(r - u), Math.round(n + c), Math.round(r + u)],
                                strokeWidth: 2,
                                stroke: "rgba(0, 0, 0, 0.65)"
                            })),
                            e.sliceTwice && (s.add(new (de().Line)({
                                points: [Math.round(n), Math.round(r), Math.round(n - c), Math.round(r + u)],
                                strokeWidth: 2,
                                stroke: "rgba(0, 0, 0, 0.5)"
                            })),
                            s.add(new (de().Line)({
                                points: [Math.round(n), Math.round(r), Math.round(n + c), Math.round(r + u)],
                                strokeWidth: 2,
                                stroke: "rgba(0, 0, 0, 0.5)"
                            })),
                            s.add(new (de().Line)({
                                points: [Math.round(n - u), Math.round(r), Math.round(n + u), Math.round(r)],
                                strokeWidth: 2,
                                stroke: "rgba(0, 0, 0, 0.5)"
                            })),
                            s.add(new (de().Line)({
                                points: [Math.round(n), Math.round(r), Math.round(n), Math.round(r - u)],
                                strokeWidth: 2,
                                stroke: "rgba(0, 0, 0, 0.5)"
                            })))
                    }
                    let g = m[a].structure;
                    if (d = e.unitBlank ? null === g || void 0 === g || null === (r = g.steps) || void 0 === r ? void 0 : r.length : null === (i = e.pips[a]) || void 0 === i ? void 0 : i.structure,
                    d && g) {
                        let a = g.mask
                          , t = g.steps.slice()
                          , n = g.start.x
                          , r = g.start.y;
                        for (a && d < t.length && a(d) && t.shift(),
                        l = 0; l < d && l < t.length; l++)
                            n += Math.round(16.5 * t[l].x),
                            r += Math.round(t[l].y * h),
                            s.add(new (de().RegularPolygon)({
                                x: n,
                                y: r,
                                radius: Ee,
                                sides: 6,
                                rotation: 30,
                                strokeWidth: 3,
                                stroke: "red",
                                fill: "white"
                            })),
                            e.sliceStructurePips && s.add(new (de().Line)({
                                points: [Math.round(n - c), Math.round(r - u), Math.round(n + c), Math.round(r + u)],
                                strokeWidth: 2,
                                stroke: "red"
                            }))
                    }
                }
                ),
                t.add(s),
                this.handleResize(),
                a.draw()
            }
        }
        const Ra = Ta
          , ja = t.p + "static/media/card-base-ba.e4913b1c1901b2ac60c7.png"
          , wa = t.p + "static/media/card-base-in.069b33efea796afadb2d.png"
          , Ea = t.p + "static/media/infantry.51dc34d3818ee75daee5.png"
          , Ba = 36
          , Pa = 28
          , ka = 15
          , Ia = {
            unitName: {
                x: 60,
                y: 60
            },
            unitDataLabel: {
                x: 60,
                y: 150
            },
            typeLabel: {
                x: 60,
                y: 215
            },
            type: {
                x: 170,
                y: 215
            },
            massLabel: {
                x: 60,
                y: 265
            },
            mass: {
                x: 170,
                y: 265
            },
            moveLabel: {
                x: 60,
                y: 335
            },
            move: {
                x: 170,
                y: 335
            },
            TMMLabel: {
                x: 60,
                y: 385
            },
            TMM: {
                x: 170,
                y: 385
            },
            antimechBox: {
                x: 600,
                y: 259
            },
            antimech: {
                x: 609,
                y: 265
            },
            antimechLabel: {
                x: 660,
                y: 265
            },
            mechanizedBox: {
                x: 600,
                y: 209
            },
            mechanized: {
                x: 609,
                y: 215
            },
            mechanizedLabel: {
                x: 660,
                y: 215
            },
            equipmentLabel: {
                x: 60,
                y: 452
            },
            equipment: {
                x: 230,
                y: 452
            },
            pilotDataLabel: {
                x: 1200,
                y: 220
            },
            pilotNameLabel: {
                x: 1200,
                y: 280
            },
            pilotName: {
                x: 1310,
                y: 280
            },
            skillsCost: {
                x: 1890,
                y: 250
            },
            rankImg: {
                x: 1940,
                y: 220
            },
            edgeLabel: {
                x: 1200,
                y: 335
            },
            edge: {
                x: 1330,
                y: 347
            },
            gunneryLabel: {
                x: 1200,
                y: 505
            },
            gunneryHex: {
                x: 1290,
                y: 446
            },
            gunnery: {
                x: 1240,
                y: 425
            },
            pilotingLabel: {
                x: 1380,
                y: 505
            },
            pilotingHex: {
                x: 1470,
                y: 446
            },
            piloting: {
                x: 1420,
                y: 425
            },
            tacticsLabel: {
                x: 1600,
                y: 505
            },
            tacticsHex: {
                x: 1690,
                y: 456
            },
            tactics: {
                x: 1640,
                y: 435
            },
            leadershipLabel: {
                x: 1700,
                y: 330
            },
            leadershipHex: {
                x: 1790,
                y: 412
            },
            leadership: {
                x: 1740,
                y: 394
            },
            gutsLabel: {
                x: 1800,
                y: 505
            },
            gutsHex: {
                x: 1890,
                y: 456
            },
            guts: {
                x: 1840,
                y: 435
            },
            troopsLabel: {
                x: 60,
                y: 565
            },
            troopsRow: {
                yStart: 800,
                yHeight: 120,
                yDmgLabel: 710
            },
            squadLabel: {
                x: 60,
                y: 710
            },
            squadNumber: {
                x: 90,
                y: 800
            },
            BA_icon: {
                x: 180,
                y: 757
            },
            BA_armorLabel: {
                x: 320,
                y: 710
            },
            BA_pips: {
                x: 300,
                y: 812
            },
            BA_weaponColumns: [{
                x: 560,
                y: 575
            }, {
                x: 860,
                y: 575
            }, {
                x: 1160,
                y: 575
            }, {
                x: 1460,
                y: 575
            }, {
                x: 1760,
                y: 575
            }],
            IN_icon: {
                x: 180,
                y: 752
            },
            IN_platoonLabels: [{
                x: 470,
                y: 710
            }, {
                x: 920,
                y: 710
            }, {
                x: 1370,
                y: 710
            }],
            IN_pips: [{
                x: 420,
                y: 812
            }, {
                x: 870,
                y: 812
            }, {
                x: 1320,
                y: 812
            }],
            IN_weaponColumns: [{
                x: 1700,
                y: 575
            }]
        }
          , Fa = e => {
            let {type: a} = e;
            const t = a === A.UnitTypeEnum.IN ? wa : ja;
            return (0,
            b.jsx)(Na, {
                imageURL: t
            })
        }
          , qa = e => {
            let {type: a, rowCount: t} = e;
            var n, s;
            a === A.UnitTypeEnum.BA ? (n = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEcAAABuCAYAAAB1Ew7hAAAACXBIWXMAAC4jAAAuIwF4pT92AAAgAElEQVR42s19d3xU15n2c6f3Js1o1DUadYQkimSqwBSbZsoaUwKEZE3iL7b3s40TXHaXrJ18wXZibxIX3DbrJAu2F9McEEUIGSTRhCWhipBGwGg0VRppRiNNv/f7A0uRYJpgCH7/mt897z33nOec87bznjMExtDzzz+/ptdi+U+BUJCKeySKouDxeCyPProkYcOGDT5EkV56acfarq6ufTExMfdcF41Gp0xG44lZs2f/+MUXXzSOLWOM/PivTz9lnTl79v2Vq1bGs9lsRAOcsrIyuN1uRJuGhoYwefJkFBYWRqM6QqPRLKmvr98OYEdAcCwWC3w+L43BYIStrbe3F3a7HQDA5XIRFxcHGo2GfywRAZ+6XC4YDUZQoAAASqUSXC43ZE1sNhuOQccdHR/t0cuvvOKRSCTvNTU1Ba3E6/XiattVAIBKpYJKpQKfz0d7ezuGhobwoKmnpwcGgwGJSYlQqVRISkqCyWSCTqcL2afaS7X2efPnfxIUHABYtWrV71pbWi9ardaAFWk0GmRkZiA2NhYEQYAgCIhEIuTk5KBbq4Xf739gwFgsFjCZTKhUKjCZTAAAk8lEWloaOBwOTCZTwPcaGhoglUr/4/nnn28LCc6jjy5xFRYVPVtVVTV8e0ftNjskEgkCLTuCIJCSmgqDwfDAwLHZbFAoFAHLYmNjR8XA7YB2dmq+2bhx4/uB3rujp6+++urlp5766ZvNzc2vjRV4/QP9iI+PD9o4LpcLj8czoQ6VlZVxay9dyu3o6EjjcrlKP+l30Wk0w9Rp067NnVvalZ+fT0Uq/AmCCMlDp9Ph9/tBp9MBAD6fD1VVVfaHSkr+peShhzwRgQMA69dv+N3uDz5YkZKSUiyVSsdVHq6RYcqJt9/+3aTGK40r7IP2BV99tW+mSCTmZ2RmEDweD36/Hw6HA01NTf6amhr9YytWVKjS00+Xls4tW7v2ib57FuFjAGxoaIBYLPnVC9u3N09M5AN4/bXXirVa7Zlly5dx6XT6LS1gNCItLS2oBiMIAiO2x3eq3LJkydKEvr6++G8qK1d6PJ7NijhFiUqloiUmJoLL5QYdcZIk0d/fD61Wi66uLpvdPvi1Uhn3xZYtW775/PPPlykUcfsKCwtG+Ts6OqBWqwNqTYqi0NnZiczMzNG2lpefqvrpT3+yaMGChZ4JgwMA27Y9+VpaWtrOyZMnAwBu3tRCLBZBIpGM43M6ndBqtcjOzh59duPGDez/ar9XoVB0xcpj1ampqQyVShVWrQabkX19fejo6KAMeoOtz9pnFwlFKctXLIdAIAAADA8Po6enBxkZGeMApygKGo0G8fHx4PP58Pl8+NvfjjhycnJmvfzyy00TNxa+o71793IPHNhf9dhjj00bAUSn08HtdoPH44FGo91S4RSFNJVqdNQMBgOam5pROq8UTCYzqjYQRVGjs6q6qhrLVywf1U4OhwP6Hj04XA44HA7cbjeGh4eRkJAAoVAIAKirq4PFbHnpg92737o7S2qsgH7llRKzxXxm+fLlnJFOkiSJ4eFhkCQJPp8/KuRGZlFZWRlWrFiBaFjaoUir1UKr1WLOnDnjnrvdbjidTnA4t0Aaob6+Ppw4fqJm7dq1C55Yty6s9qCHY6iqru7Jn5TPpihq3oiqJAgCLBYLbDZ73KygKApnzpxBSUkJxGIxAECv16OtrQ0mkwkulws0Gg1sNjusdhkhn8+H3t5edGu70XW9C729vRAKhWCxWBCLxdBqtaDRaBCJRH/XMgwGOBzOOLPD7/fj5MmTjuys7MeffuYZfSTfZkTCNH/+/F1HjhxZnpycPHWk04FIp9NBIBCM2ht1dXXgsJiYO3sWmpqb8ekn/wUGgwGlMg75k/ORmpqKuLi4cTOMoijY7Xbo9XpoOjVoamqC2+2Fz+fBr3/1H/CTJMrLK1BcUoKYmBgUFxfjyJEjiIuLG11egaixsREMOuPXO3/5y8ZIZyY9EqbDX3/te2zlysarbVc3Z2ZmMgKNOkmSqKysRGlpKRgMBm7e1AKUH48sXgSBgI/a2suw2QYhFIpAkhR03TrUXrqMc+fPwWq1wuPx4Pr16yg/WY7jx05Ao+mCwzEMLpc3KkhnzChBukqF7OwslJUdQ1paGthsNthsNowGIxRxgY1Aq9WKqrNVNU888cTTX3z5pT+q4ABATU2NLjsnh0un0UvlCnlAVe73+5GamgqPx4OLF85jzeqVYDAYcLlc+O///gvYbM7osqTTGeByueByuBjot+Hq1Xb09PSAJAGBQHDHkqXT6RCJhMjKzASLxYJMJkN9QwOSkpIgFotx8eJFZGdn37Fc/X4/yk+WOzIzM5/42dNP90wonDER5tWrVu06f/58fSBT3OfzgcPmgKIoNDQ0IDcnGywWa9S5m1JUCIvFFNCKptPp4PP5YLM5d3SOoig4HA6QpA/iMXIlISEeN29ch9VqBY1GAxFEtzQ1NYECdr3+q181RMfvD0HbX3hh1qBj8PSyZcvYY0e239qP/Qf2QygQIjUtFZMmTYKQz0NyctJoJ41GE2rOncPJk6fA4/HB4QS3eUiSxODgIGQyMZYtW4KiwiLw+bzRuurqG8Dh8lBRUQFQt3qyZs2acXX0W/tx6PDh81u3bl2wZs0a130HBwDWr1v3m0n5k15hMVnQdGngcrlQUlKCU6dO4Yc//OGolrD29aKwYHIAGdCPS5cu4WjZcQA08Hi80Rnj9/thsw0gPT0Njz6yGJMm5Y3OwFEn2G5H1w3tqDV+48YNGPR6UABMJhPEYjGys7NRW1s7FB+fMPc3v/lN/d30k3E3L6Wnp3dcuHCBWrhwIfHII4+AJEl89OFHKC4uHqc+3R4vSJK8wwiUyaRYsuRRzJkzG/X1DThadgw2mwMejxvTphZh4cIfIiMjY5z9NG5GDAyMU90ymQw1NTVISUnFqlWrMDQ0hKamJphMpp7p06fboxtOC0LvvPM2UV9f/6JIJHpj3rx59LEq+OzZsygsLMRYVW82m5GXkxXWZXC53bjadhVSmRTJSUlhLeprHZ3gcHnj5FNt7WWkpqSM01hGownffPONTiIWL9v94YdNE44vR8p4+nQFce7cue0xMTFvLFy4kH679ZuQkACLxTLuGZ/PDxhHuZ04bDaKigqRmpISkavh8/nuENwmoxGyGNm4Z0plHJYuXZJkNBqP7vjFL/LvGzhHj5ZtS0hIeLO0tJQeaLqLxWIMDAzcEeNxOKIfPnXfpvEoioKf9CNYu1avWZ2s69GV7dq1KzHq4Lz/3nsSi9n8/4IBMxKkdrlct2170CYcAAtHfr8fXq/vjmdMJjOoSyKRSDBjxozk+vq6V6IOTkNDw7qs7Cx5KPP8lgAjAsiT6IIzMGADj8eb8HvJycng8wWb9+zZI4sqODqdbklqauh9PqfTCS7vTsHr8/ujOnv6+/tHww9jjUivxxsyEkmj0ZCSkiyurq5+OGrgHD9+nKWIi5t5e4MC+S8ymSzglDabzVEDx/mdZ397+JPFZoUdhLi4OFjM5pKogfPlF1+wWSxmTLgQQ1dXF5RK5Z2aiMOBzWaPCjAejyfoMk1NTUVPT2jXSSAQwGA0xEcNHIIggDB7AGazGUKhcFxgafxou6OyLazT9SDY/nh6ejquXGkESZJRM+zCgrNlyxanw+G4HmzKut1uVFdVY9q06UHriJXL0dZ2FYODg3C73SBJEiRJgqKogHJi5DlJkvD5fHA6nejt7YN1YCBozIbD4SAvNxf1dcE9BYvFguSUlPaoWsjPPvPMkz6f78O5pXMZIwHtER+n4lQFZs+ZPW5Drb+/H0NDQ0hKShp95vV6Ybfb4fN6QdBowBhgCIIAj8eF2+2Gz38LNAL4O993nReJROPUdWtLK7Kys0ZdFoqicOnSJRAEgWnTpo3aPRRFQafToeJURdeiRYvmPfPss7qoug/bX3hhid5g2BUTIytKTEiEzW6Dtc+KuaVzx7kMfr8ff/3rX/3Z2dn0mTNnRjyFfT4f6HR6xOFTv9+P/3znHf+ixYvpRUVF43cbOjW40ngFWZlZ8Pq86Ozs9LCYrL25eXk7d+zY0R31YNf5Cxc6i4uns+Ry+VK5XA6FQoGioqI75ExnZyfsdvunfp+/MCMzI2ILnEajRQwMcCsN5cb1GyeMBqM/Nzc3dmT2EAQBWYwMGRkZIEkSIpEIOp3OUTRlyuqf//znekRT5ozQsWPHGLYB25MFBQVISkqCXC6/ozM+nw8N9Q2Whx9e8PrQ0JAhnHC8N2NwAAwG41tFXNzbrS2td5SzWCwkJSUhPj4e+fn54itXGrbeN9/q5MkTD6er0wuCaaSRWSORSj7cunVrT5+179vh4eH7Bk5vby/i4+Mbly1btkfTpbnmdDqD8qpUKgwPO3986NBBVtTBqaioILRa7U/y8vKCznuf14fm5hZz6dzSdwEgNia27nYvPZpkNBo9CQkJ51evXu1MSEj4bXNzS1BeNpuNdJUq+9y580ujDk7dt9+qZDLZY4Es4L/HWK5heGjot+s3bLAAgFwuP9PTo6fuBzBerxdms/kqn8/XA8DSpUv/50pDQ32omZqTm0N0dnQ8+b//+yURVXAamxr/WalUcoIJTK/Xi/q6+u6ly5Z9OvJs4cJFlw0Gg/F+yB2TyQShUHj6/z73HAkADz+8wKVQKN5samqiQlnHBI22xGy25EUFnOrqauaWzZs/93q8K0NZuO3t7VAqle9v27ZtNKCzdNnSYbfLdeB+JDS1t7eT2VnZ+8Y+27Bx48Hr1683Bku/oygKg4N2srtbOz0q4Jw8eWKGRCpZP3PWrMljbYmxdOXKFbS1tvXMnj37w9vLsrOzd9d9W+eK5uyxWq3Q6/WnZ8+efWHs88WLF3vS0tLePHq0jDIajQG118qVK9nX2q9tOXbsGHHP4NTX1a/Jzc0l0tJSwefzAxpuFy9edGXn5HxcUFh4x5AtXLSodWBg4OTtEcJ7nDWIi1Punjd//h2Ib9q0+YBIKKzSaDRBYzrKeGVpe3u76p7Aqays5IjEorWBPO2xhtuKFSs4ly5d3GE0GES3l3dcu0b4/L60sTsF90oKhQK9Fos6sAYzeExm06BKpQql1pm1ly6tvidwDh08WJqUlJQULCw6Ao5QKASTyTzT29vbH0AIJinjlLmR5DZHSnK5HG63e0agskWLFlN0Ov344OBg0PdTUlJAkuT6o0eP0u4aHIvFsl6tVoddmwa9HmKxuPyJdevu0BSnKyunxymVzGgKY6FQCIFAMOPgwcAGXUlxSYVWqw2aLMDlchETGzPt228vZ98VOF8fPiwgCGK5XC4P29ibWq0/MyPzZMA4j8n0UFyQzIe7pe98J+W19vaAnWMwGO0GvaHN6/UGrUOtVtM7OjqeuCtwDh46uECVrlKE20Py+Xwwm83t+fn5d8RI9n/1FUGj0WbGxsZGXZUnJCTQOjo7ZwUqe2H7dpLFYp0OZZ0nJibC4/E8vnfvXvqEwXG5XBvT09PDLimLxQK/z39q5apV/gAqVyiLkU25H6lvcrkcen1PUHtFJpMd13XrqFDuhFKpzG9pbiqcEDifffaZlE6nPxrKVRih7u5u5OXlVQYq6+jsLFYoFPz74T5IpVKIxeI5n+/dG3BwH3nkkXMGg8EeajciQ51B0+l6NkwInPq6uscyMjKk4WIrFEVBrzfYMzIzA4LTo9PNUCqVxP0Ah06nQywSp9vs9qRA5atWr7aZzebKUForPiEeTpdz1fvvv0ePCJzy8nJC19PzT6HshBFyOBwYHh6uVqvVAbcWbHZbSSSz766XlkLOunjhQnFQuZKU+I1eHzy2xWQykZycnKnv0c+OCJzm5ia5QMBfECopcoT0ej14XG75nDlzqMDrPuZ0XV3dffHKh4eHUVdX1x2njGsNxpOWpjqmvakNeUJQrc4gOjs7H48InK6ursezsrKEkYQrb9686cvKzj4ewgselslk92VZcTgciMVizpSiKaZgPFlZWZo+a9/VUCpdqYwDCKw+e/YsNyQ4VVVVhEFvWNHX1wej0RjyEIjX64XZZG6XyWTXAlrXhw7RurXazRkZGfdlSdFoNOTl5sqPnzi+NhjP448/7h8eHj4RSqV7PB5wOdzkEydOBNwiHrXr586dSx08cOCpt995u7H+SqMUJImcnBykpabeSo8XCUdjxhaLBRwu9/RTTz0V0N1uaKifmqZKmxPIWY0WqTMy0NzS8uTRo0c/Xb58ecB25E/Kr+zWdm9PSEggxgTJ0NOjh0bTCW23DkNDQ8ifPJkZEhwAOHf+fDFBY0iSklMAAP32QWhrzsE2MIAYmRTZ2VlITkrGjZs3KJlUeiJYw6+2Xf1R6bzS+3rok8fjQaFQTG9taXkIwPlAPOlq9ZmKilP9HA5HduPGDVzrvJURJhQJwecLoM7MwkB/P1FTXT0TwOGQMqettXVDjFxOjJXospgYqNRqCCVSNLe2Yc/ePW29vX2Vjzz6aHWgBp04flzC5rDXhzq4Fi3KycmhVdfUrA9Wnp6ePkQQxJ6Tpyrg8vmhUmcgPiEBAsHfVwGPz4fBaFj9y507pwcFZ/cHHyTZBwdXjN3RvN2ncbvcKCkpeffPf/7zwuXLl9sC8X3++ecrVCpVbDjXI9zOhM/nC5s1ER8fDx6Pu+HLL78MqF4XLFhATSma8i6Xw3aOBNysfX0gyVvylCTJWyo9VZVdVV39zfbt259va20dtXtGf0gkkiddHu8KYZDYC0VRGLQNuB955NFnDx8+bA8CDNHY2Pi7WbNmqsO5DcePH0dXVxd8Ph9YLBY4HA78fj9MJhPa29tRcaoCUqkUIycFgw2Y1+MVXL16teXSpUsBzzSUl5dbN2/e3Ha1rW2tUCym9fZa0GsyOS0WM5NOoN9qtXLEEikhFItZ165dW1J99uyCkuLi2Lff/t0V2q0KTtKtVuvmUCf8XS4XuFzuWQ6bHTTPw2Q0ZsTGxswPl8tDkiQ8bk9XUWHRpJbmlmcPHjh4cP9X+6179+xtKzta9v5A/8Da3Lzc9b29veEFs1qNHp1u48EDB4KaDZmZmQfZbNY5r9cLgUCIhPj4XR9/9JH69ddfUxZOnrzN2KNz+f1+JKekgiMQzjGYzG/99a//83sGAFRXVZfY7Pai2LjgUb+B/n5IhILDP9i0Kahh19jYuHFS/qSw8RuXywWdTtf0f372s1YArQDe37t3D4PFYpNr164lAeD9995La21r9SPMlrVQJESsPHahtb8/HUDA+OiWLVuolY+tOGy32eaKRCL0mU3/cuzYsfJXXnmlC8CfXn75JWN1zbmDKnUGi8ViQZmQAJPRsJwGAK1trZtkMbEhhYRzaMhbWlpaFqz8wIH9dGu/dXVycnLY0XY6nRCJRePSvX7wg02+EWAAYGhoyOD1eMMm9RAEgaysLPaJE8dXhR4Q9xBJkmCyWBCIJfLTFRVbRmPLScknBHy+bkQWOQYHwWaxmmmHDh0UWa39T4RyGdwuFxQKeW1WdvbNEOp7empqamEkIYrvrlToCdNrn7Xfagx34vhW4DwFdDpj4/79+4MO8PTp0ztdzmGSJEk4HA4kJiZ2jfqBNtt8l9udRqPRYdD3gPR5ji5ctPBntMrKylU+klTQQsSKBwYGwOPxDi1ZsiToHsvFSxdXZWREllXh9XoxKX9SSFU0OT+fEgqFvkjA4XI5kMmkRRpNZ9ANu81btlTIY2M/GrTbQZIkeDzeDQDYuXOn6syZM7+MiZXT3G43eGx2w7p16x9/7rnnNbTWltZ1sbGhw6FDjkF/UlLi4WDlVVVVDDqNvjJS28br9eKb06dDZlFWV1dTba1t+kj3vNRqNePKlSsrg5Xn5eVRBZMnvzPsGOxlMpmw2WxzPty9m1VfX3+cxeXN5fH56DWbyPzJ+a9s3rzZDQA0Hp//MDdEXq/H40GsTNa4aNHizmA8J0+cyE9OSc4Nl6c81iyITwidTN7S0gyfz0tGMnNGQp9Op3PZp598ElRr/fvOnZ1ZWVlrPC6nuX+g/6GMjIz4QYdDLZFKQVEUeFzuYFHRlNH4FC1GJjvUpenEwEA/fL47PXzbwAD4AsHhxYsXBx1Ck9m8LCUlJWJ3gaIo8PihE62D3ZsRylNXKBQlLrdbGYrvgw8+qF61atXspKQkncls4pF+/xBFktDeuEEmJiR8lJGRMbrcaY+vXfvPJdOmraV8vg+sFnOzpqOd0vfo4BgchNM5DNfwkK+oqPBgsI/V1l4ibAMDs+Li4iZk+odbLj6fD5HOmr+HIJTMixcuzAjH99xzz3Vu+sGmDVVVVZv4QpHIZDIiTh7z7py5c16eOnXq6EcZy5cv9wDYf2vDYB+tt7dPVV1VtcBkMs3RG/T8FStWHF60aHET8FLADzU3txAEjciciAdOEAT6g1xDMybMCo/HOyFwZDIZaow12ZHwOl1OeWdH51Mer9efk5P96Y9/9ONXZ86aRQX1yteufYL8zpDSAPjk1tpvxZtvvhVqrdMkYoloIvl8NBoNIrE45Jp59d/+He/+8Y+8idTLYDDQ3NQY0Qsnjp9YIZZITuZPmvTuho0bL+bm5lIRbc1MhBoa6kmz2dw3kSXAZDCRm5sbFyZGTUhlUtlErnrwer2YO29eRLxFRUWf7d+/f9Nrr79+IRAwUQFnx46XyMHBQU2onLw7dg8YdFzv6grJU1NdBbvNPqEMU5vNBj5f0BUJ79Yf/Sjs+fKoBKQSExPrJnL4w+VyITEpOSSaRVOmgMlkOidy1ZVer/fOeOih2qiFY6NRSVpa2sFr7dciugvQ7/ejrbXNLRaL/haKb/PmLaRQJDrW2dkZURscDgcsFss5qUx643sFTkZGRqfJbDKFC045HA6cPHnSxxfwX3377Xeuhqt31syZb1y92n6+ob4hrFrX6w0QCoTfrlu3nvxegXO68vTzRUVFibef/w5k/A30DzROKZry+0jqfXLbNltBQcEOg9FAhpM96ekqUKC2vfXmm9nfG3D+8uc/0/qt/T8Ye+tS0NiLUIg4ZVxRR0fHrEjrP3/u3JbCwsKw7WQwGMjLyxO1XW1b870B54dbt5IcLrc80oRsp9Pp5fH5ukjr9/l9N13OyG5a6OnpISfnTy7/Xi2rSXl5h7o0XWENnaGhIfT29tZkh4gL3RGHmTb9UKemM6yw93g80Ov1TTm5OQ3fK3BcbjeHxQ5/rMB368izZe3atRFbjElJSWafzxeWn06ng8lkcqN53iIq4FxtayuOJN1EIBTA7/Nnfrh7d8TfvXjxYqY4jKsxAo5EIkm3WHqTvzfgfPHFF4Tb7X4okvQ2Op2OmNiYTL6Az4m0fj9JFkSakKBUxjMuXrxQ8r0BR6FQsGUy2UOReuVisZjfpenKjLR+k9GYdfu9hMEoLk4Bx6BjxvcGnLNnz+TKYmQxkfpAMpmMdv369ZxIeI8dO0aQFJUjEokjrRskRc7Yv38/8b0A5/r16zOVSmXE9UglUnh9vkmR8HZ1aWgCPj+Py41sFbJYLEgl0gK7bUD0vQDHZrNPjyRfeXRZScSwWvuyIuGVSKRyvoCfEGnYgiAIyBVyXsOVxikPHJx9+/bR2Gx2SSRpciPE5/MhEokKPvvss7DfvlxbmxcTEzOhDPi4uDjCYDCUPHBwfF6vUiqRZE0kEE6n0yESilRer1cYjre3t3fSRFPnYmJiMDzkmPbAwamtrZ0SK4+d8NkGiVTCvnnzRli5M2AbyA2VZRHMfxOJxNM/+fhj+gMF56ZWWzAReTNCsbGxhEbTNSmcpuJyuEUTWbLArfi0WCJOptPpiQ8UnOEhx+SJjuyIyrVa+wpC8ZAkyeNwuTmRbhTeBj6zrr6u4IGB86c//YnG5fImBcsEC7msxGJIxJKp31RWBpUnN2/eyI2JkUkmEkMeC36/tT/vgYHTpdHQeHye4m4ugu6zWgECbfMffjioQ+lyujqt1n7b3fxdAo/Lg91uj31g4BQUFPhdTpd2oldO+Xw+1FTXuIqLS/4Qim/7iy8OsFmsj1paWibctgHbAMRi8c0HBs669espGp22v6Ojc0Lv0el0yBVydnt7e0gX4syZbwjH0NCEBb7f70dzc7Nj2vRpRx8YOGfPnuUBmM1mT+h6CBAEAbVaTej1Pbmh+Gpqamgejzsz1AHcQERRFHg8PstoNM17IOB8tW8f7dNPP3mnoKBg5cjfBUyE2Gw2mExWyGQekUjMiI2VJ0xUIDMYDCxatJDVa7Hsfumllxb+w8GpqKh4SqFQ/DQ/P/+uPsrhcED6/SEFplQqkVAkeVeHZ1ksFhYuWsjVam/+5a0330j7h4Gza9euaU6X862ZM2cSd6NmR2YOAPmxsrKgFWg0XXIuj3vXVi6fz8f8+fMTLtVe/ris7CjzvoNTXl7Orvv223fnzZsnuJez4gwGA37SLztz9gwRwlSI5fF49xSXUSqVyMnOXnT48NdP3XdwDh069OOc3JyZ93oCjyAIKOOUiTJZTNDvEzRa/L2CAwBFU4qIIYdj55tvvBF338DZu2cP32YbeGXkr1XuFRw6g85LV6mCeuZej0d+N3+9cjsxmUxMnTpVrtFofn7fwKmpqXlcrVanROsoNIvFYhqMhqDnCTxejzzUFVgToTRVGpwu59Yjf/ubOOrgXLhwgTAYDP+kVqsRLeLxeDSNRhPUwuvrs0qjBQ6dTkdamir2yJEjC6IOztmzZxgCgWBmtG4zGRwchK5bZ0pMSDSFcE86WltbqYkmTQajxMQEwmw2zY06ODExMUqBQCC7W9U9lpxOJ44eOdKXk5v7xC927AiahfXkk0++29fb99va2tqoACQSiTA8PJwWdXC6td0CJot5z8F4j8eD8pPlTnVG5tadO3dWh+LNz88nX9i+/d8sFsue5ubmewaHwWDAYunlRB2cNJUqlslkEsG8bJvNFpE3XllZ6ecL+Nt+/etfR+QUFhYWeosKiwkZTLEAAAFESURBVJ5sb28/EmmGV7B/kqTRaCgpKUlsaWmhRRWcHp3O7PF4qECy46t9X6G7O/R1nyRJ4uzZKsrtcj/3xz++u3cio/f0M894lixZuqmmuuZMuO9QFIWvv/4aly9fviMJnCRJXLt2zXj58mUqquAUlxT39Fp6+7q6ujA4OAiKotDd3Y1Dhw5pKFB/CNfgCxcuUKTfv+vVf/3XD+5mSWzatMm+bt26jafKT9UF+z/OEeJyuVaD3vB6WVmZe3h4GD6fDxaLBY2NjUhKSurcunVrxOBELGF/8pNtxTabbfHQ0NBUqVQ6m06jXymaUvSjsqNH5wiFon2xsTFB5IwXLDbrY3W6+mcvvfzyPeXr/eH3v0+vra09xeVxVYEaTt2Sj+bk5OTEpOSkRzUazSeD9kGTx+u9xGazvl20cNHhp595xhTp9/4/84kOdQKX+FEAAAAASUVORK5CYII=",
            s = Ia.BA_icon) : (n = Ea,
            s = Ia.IN_icon);
            var r = [];
            for (let i = 0; i < t; i++)
                r.push((0,
                b.jsx)(Na, {
                    imageURL: n,
                    x: s.x,
                    y: s.y + i * Ia.troopsRow.yHeight
                }, "unitImg" + i));
            return (0,
            b.jsx)(ue.Group, {
                children: r
            })
        }
          , Xa = e => {
            let {rank: a} = e;
            var t;
            if (1 === a)
                t = Se;
            else if (2 === a)
                t = be;
            else if (3 === a)
                t = Ce;
            else if (4 === a)
                t = Te;
            else {
                if (5 !== a)
                    return null;
                t = Re
            }
            return (0,
            b.jsx)(Na, {
                imageURL: t,
                x: Ia.rankImg.x,
                y: Ia.rankImg.y
            })
        }
          , Na = e => {
            let {imageURL: a, width: t, height: n, x: s, y: r} = e;
            const [i] = ce()(a);
            return (0,
            b.jsx)(ue.Image, {
                image: i,
                width: t,
                height: n,
                x: s,
                y: r
            })
        }
        ;
        class Wa extends n.Component {
            constructor(e) {
                super(e),
                this.container = null,
                this.setContainerRef = e => {
                    this.container = e
                }
                ,
                this.handleResize = this.handleResize.bind(this)
            }
            render() {
                var e;
                return (0,
                b.jsx)("div", {
                    className: "card-body mt-0 pt-0",
                    children: (0,
                    b.jsx)("div", {
                        ref: this.setContainerRef,
                        children: (0,
                        b.jsx)(ue.Stage, {
                            ref: this.props.stageRef,
                            width: this.props.width,
                            height: this.props.height,
                            children: (0,
                            b.jsx)(ue.Layer, {
                                listening: !1,
                                preventDefault: !1,
                                children: (0,
                                b.jsxs)(ue.Group, {
                                    children: [(0,
                                    b.jsx)(Fa, {
                                        type: this.props.data.unitType
                                    }), (0,
                                    b.jsx)(qa, {
                                        type: this.props.data.unitType,
                                        rowCount: this.props.data.unitType === A.UnitTypeEnum.BA ? this.props.data.squadSize : this.props.data.squadCount
                                    }), null !== (e = this.props.data) && void 0 !== e && e.pilotBlank ? null : (0,
                                    b.jsx)(Xa, {
                                        rank: this.props.data.skillsRank
                                    })]
                                })
                            })
                        })
                    })
                })
            }
            componentDidMount() {
                this.handleResize(),
                window.addEventListener("resize", this.handleResize),
                this.renderData(this.props.data)
            }
            componentWillUnmount() {
                window.removeEventListener("resize", this.handleResize)
            }
            componentDidUpdate(e) {
                this.renderData(this.props.data)
            }
            handleResize() {
                if (!this.props.stageRef)
                    return;
                const e = this.props.stageRef.current;
                if (!this.container || !e)
                    return;
                const a = this.container.offsetWidth
                  , t = a / this.props.width
                  , n = Math.round(this.props.height * t);
                e.size({
                    width: a,
                    height: n
                }),
                e.scale({
                    x: t,
                    y: t
                })
            }
            renderData(e) {
                if (!this.props.stageRef)
                    return;
                const a = this.props.stageRef.current;
                if (!a)
                    return;
                const t = a.children[0];
                if (!t)
                    return;
                const n = t.children[1];
                n && n.destroy();
                const s = new (de().Group);
                e.unitBlank || s.add(new (de().Text)({
                    x: Ia.unitName.x,
                    y: Ia.unitName.y,
                    text: e.unitName,
                    fontSize: 66,
                    fontFamily: "vegas-regular",
                    width: 1060,
                    wrap: "none"
                })),
                s.add(new (de().Text)({
                    x: Ia.unitDataLabel.x,
                    y: Ia.unitDataLabel.y,
                    text: "UNIT DATA",
                    fontSize: 44,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: Ia.typeLabel.x,
                    y: Ia.typeLabel.y,
                    text: "Type:",
                    fontSize: Ba,
                    fontFamily: "falcon-bold"
                })),
                e.unitBlank || s.add(new (de().Text)({
                    x: Ia.type.x,
                    y: Ia.type.y,
                    text: e.unitTypeName,
                    fontSize: Ba,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Text)({
                    x: Ia.massLabel.x,
                    y: Ia.massLabel.y,
                    text: "Mass:",
                    fontSize: Ba,
                    fontFamily: "falcon-bold"
                })),
                s.add(new (de().Text)({
                    x: Ia.mass.x,
                    y: Ia.mass.y,
                    text: e.unitBlank ? "       Tons" : e.mass + " Tons",
                    fontSize: Ba,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Rect)({
                    x: Ia.antimechBox.x,
                    y: Ia.antimechBox.y,
                    height: 40,
                    width: 40,
                    stroke: "black",
                    strokeWidth: 4,
                    cornerRadius: 1
                })),
                e.hasAntiMech && !e.unitBlank && s.add(new (de().Text)({
                    x: Ia.antimech.x,
                    y: Ia.antimech.y,
                    text: "X",
                    fontSize: Ba,
                    fontFamily: "falcon-regular",
                    fill: "#000000"
                })),
                s.add(new (de().Text)({
                    x: Ia.antimechLabel.x,
                    y: Ia.antimechLabel.y,
                    text: "Anti-Mech Attack",
                    fontSize: Ba,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Text)({
                    x: Ia.moveLabel.x,
                    y: Ia.moveLabel.y,
                    text: "Move:",
                    fontSize: Ba,
                    fontFamily: "falcon-bold"
                })),
                e.unitBlank || s.add(new (de().Text)({
                    x: Ia.move.x,
                    y: Ia.move.y,
                    text: e.move,
                    fontSize: Ba,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Text)({
                    x: Ia.TMMLabel.x,
                    y: Ia.TMMLabel.y,
                    text: "TMM:",
                    fontSize: Ba,
                    fontFamily: "falcon-bold"
                })),
                e.unitBlank || s.add(new (de().Text)({
                    x: Ia.TMM.x,
                    y: Ia.TMM.y,
                    text: e.tmm,
                    fontSize: Ba,
                    fontFamily: "falcon-regular"
                })),
                s.add(new (de().Text)({
                    x: Ia.equipmentLabel.x,
                    y: Ia.equipmentLabel.y,
                    text: "Equipment:",
                    fontSize: 32,
                    fontFamily: "falcon-bold",
                    verticalAlign: "top",
                    lineHeight: 1.1
                })),
                s.add(new (de().Text)({
                    x: Ia.equipment.x,
                    y: Ia.equipment.y,
                    text: e.equipment,
                    fontSize: 32,
                    fontFamily: "falcon-regular",
                    width: 880,
                    height: 120,
                    verticalAlign: "top",
                    lineHeight: 1.1
                })),
                s.add(new (de().Text)({
                    x: 1155,
                    y: 58,
                    text: "Gunnery",
                    fontSize: Pa,
                    fontFamily: "falcon-bold",
                    width: 180,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 1290,
                    y: 58,
                    text: "Anti-Mech",
                    fontSize: Pa,
                    fontFamily: "falcon-bold",
                    width: 180,
                    align: "center"
                })),
                e.unitType === A.UnitTypeEnum.IN && (s.add(new (de().Text)({
                    x: 1430,
                    y: 120,
                    text: "Platoon 1",
                    fontSize: Pa,
                    fontFamily: "falcon-bold",
                    width: 180,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 1430,
                    y: 219,
                    text: "Platoon 2",
                    fontSize: Pa,
                    fontFamily: "falcon-bold",
                    width: 180,
                    align: "center"
                })),
                s.add(new (de().Text)({
                    x: 1430,
                    y: 321,
                    text: "Platoon 3",
                    fontSize: Pa,
                    fontFamily: "falcon-bold",
                    width: 180,
                    align: "center"
                })));
                const r = e.unitType === A.UnitTypeEnum.BA ? e.squadSize : e.squadCount;
                s.add(new (de().Text)({
                    x: Ia.troopsLabel.x,
                    y: Ia.troopsLabel.y + 30,
                    text: "TROOPERS & WEAPONS",
                    fontSize: 44,
                    fontFamily: "falcon-bold"
                }));
                for (let g = r; g > 0; g--)
                    s.add(new (de().Text)({
                        x: Ia.squadNumber.x,
                        y: Ia.squadNumber.y + (r - g) * Ia.troopsRow.yHeight,
                        text: g,
                        fontSize: 32,
                        fontFamily: "falcon-regular"
                    }));
                const i = 7.5
                  , l = ka * (Math.sqrt(3) / 2)
                  , o = 16.5;
                var m, c;
                if (e.unitType === A.UnitTypeEnum.BA)
                    for (let g = 0; g < r; g++) {
                        var u;
                        m = Ia.BA_pips.x,
                        c = Ia.BA_pips.y + g * Ia.troopsRow.yHeight,
                        s.add(new (de().RegularPolygon)({
                            x: m,
                            y: c,
                            radius: ka,
                            sides: 6,
                            rotation: 30,
                            strokeWidth: 3,
                            stroke: "red",
                            fill: "white"
                        })),
                        e.sliceStructurePips && s.add(new (de().Line)({
                            points: [Math.round(m - i), Math.round(c - l), Math.round(m + i), Math.round(c + l)],
                            strokeWidth: 2,
                            stroke: "red"
                        }));
                        const a = e.unitBlank ? 6 : (null === (u = e.pips.Body) || void 0 === u ? void 0 : u.armor) || 0
                          , t = e.baorangePips
                          , n = e.barainbowPips
                          , r = e.bagreenPips
                          , o = e.babluePips
                          , h = e.bapurplePips;
                        let d = "black"
                          , p = "white"
                          , y = 3;
                        r ? (d = "green",
                        p = "rgba(0, 255, 0, 0.10)",
                        y = 4) : o ? (d = "blue",
                        p = "rgba(0, 255, 255, 0.15)",
                        y = 4) : h ? (d = "rgba(41, 0, 85, 1.00)",
                        p = "rgba(127, 0, 255, 0.10)",
                        y = 4) : t ? (d = "rgba(233, 116, 0, 1.00)",
                        p = "rgba(233, 116, 0, 0.15)",
                        y = 4) : n ? (d = "black",
                        p = "rgba(0, 0, 0, 0.2)",
                        y = 1) : (d = "black",
                        p = "white",
                        y = 3);
                        for (let u = 0; u < a; u++)
                            m += Math.round(33),
                            s.add(new (de().RegularPolygon)({
                                x: m,
                                y: c,
                                radius: ka,
                                sides: 6,
                                rotation: 30,
                                strokeWidth: y,
                                stroke: d,
                                fill: p
                            })),
                            e.sliceArmorPips && s.add(new (de().Line)({
                                points: [Math.round(m - i), Math.round(c - l), Math.round(m + i), Math.round(c + l)],
                                strokeWidth: 2,
                                stroke: "rgba(0, 0, 0, 0.65)"
                            }))
                    }
                else
                    for (let g = 0; g < 3; g++) {
                        s.add(new (de().Text)({
                            x: Ia.IN_platoonLabels[g].x,
                            y: Ia.IN_platoonLabels[g].y - 10,
                            text: "Platoon " + Number(g + 1),
                            fontSize: Ba,
                            fontFamily: "falcon-bold"
                        }));
                        for (let a = 0; a < r; a++) {
                            const t = e.squadSize;
                            m = Ia.IN_pips[g].x + (7 - t) * o,
                            c = Ia.IN_pips[g].y + a * Ia.troopsRow.yHeight;
                            for (let a = 0; a < t; a++)
                                m += Math.round(33),
                                s.add(new (de().RegularPolygon)({
                                    x: m,
                                    y: c,
                                    radius: ka,
                                    sides: 6,
                                    rotation: 30,
                                    strokeWidth: 3,
                                    stroke: "black",
                                    fill: "white"
                                })),
                                e.sliceArmorPips && s.add(new (de().Line)({
                                    points: [Math.round(m - i), Math.round(c - l), Math.round(m + i), Math.round(c + l)],
                                    strokeWidth: 2,
                                    stroke: "black"
                                }))
                        }
                    }
                const h = 40;
                var d;
                e.unitBlank || (e.unitType === A.UnitTypeEnum.BA ? (d = Ia.BA_weaponColumns,
                e.weapons.length > 5 && e.weapons.splice(5)) : e.unitType === A.UnitTypeEnum.IN && (d = Ia.IN_weaponColumns,
                e.weapons.length > 1 && e.weapons.spice(1)),
                e.weapons.forEach( (e, a) => {
                    s.add(new (de().Text)({
                        x: d[a].x,
                        y: d[a].y - 20 - 7,
                        text: e.name,
                        fontSize: 32,
                        fontFamily: "falcon-bold",
                        width: 300,
                        align: "center",
                        height: 70,
                        verticalAlign: "middle"
                    })),
                    s.add(new (de().Text)({
                        x: d[a].x - 90,
                        y: d[a].y + h - 10,
                        text: "PB\n" + e.rangePB,
                        fontSize: Pa,
                        fontFamily: "falcon-regular",
                        width: 300,
                        align: "center",
                        wrap: "none",
                        height: 300,
                        verticalAlign: "top",
                        lineHeight: 1.4285714285714286
                    })),
                    s.add(new (de().Text)({
                        x: d[a].x - 30,
                        y: d[a].y + h - 10,
                        text: "S\n" + e.rangeS,
                        fontSize: Pa,
                        fontFamily: "falcon-regular",
                        width: 300,
                        align: "center",
                        wrap: "none",
                        lineHeight: 1.4285714285714286
                    })),
                    s.add(new (de().Text)({
                        x: d[a].x + 30,
                        y: d[a].y + h - 10,
                        text: "M\n" + e.rangeM,
                        fontSize: Pa,
                        fontFamily: "falcon-regular",
                        width: 300,
                        align: "center",
                        wrap: "none",
                        lineHeight: 1.4285714285714286
                    })),
                    s.add(new (de().Text)({
                        x: d[a].x + 90,
                        y: d[a].y + h - 10,
                        text: "L\n" + e.rangeL,
                        fontSize: Pa,
                        fontFamily: "falcon-regular",
                        width: 300,
                        align: "center",
                        wrap: "none",
                        lineHeight: 1.4285714285714286
                    })),
                    s.add(new (de().Text)({
                        x: d[a].x,
                        y: Ia.troopsRow.yDmgLabel,
                        text: "Dmg",
                        fontSize: Ba,
                        fontFamily: "falcon-regular",
                        width: 300,
                        align: "center",
                        wrap: "none"
                    }));
                    for (let t = r; t > 0; t--)
                        s.add(new (de().Text)({
                            x: d[a].x,
                            y: Ia.troopsRow.yStart + (r - t) * Ia.troopsRow.yHeight,
                            text: e.damage[r - t],
                            fontSize: 32,
                            fontFamily: "falcon-regular",
                            width: 300,
                            align: "center"
                        }))
                }
                ));
                t.add(s),
                this.handleResize(),
                a.draw()
            }
        }
        const za = Wa;
        var Ga = t(5513);
        class Oa {
        }
        Oa.ArmorAlias = {
            laarmor: "LA",
            raarmor: "RA",
            ltarmor: "LT",
            rtarmor: "RT",
            ctarmor: "CT",
            hdarmor: "HD",
            llarmor: "LL",
            rlarmor: "RL",
            rtlarmor: "LTR",
            rtrarmor: "RTR",
            rtcarmor: "CTR",
            fllarmor: "LFL",
            frlarmor: "RFL",
            rllarmor: "LRL",
            rrlarmor: "RRL"
        },
        Oa.ArmorTypeAlias = {
            hardened: "hardened",
            ferrolamellor: "ferolam",
            ballisticreinforced: "ballreinf",
            reflective: "lasrefl",
            reactive: "reactive",
            stealth: "stealth",
            stealtharmor: "stealth"
        },
        Oa.StructureTypeAlias = {
            iscomposite: "composite",
            isreinforced: "reinforced"
        },
        Oa.WeaponAlias = {
            isac2: "ac2",
            isautocannon2: "ac2",
            isac5: "ac5",
            isautocannon5: "ac5",
            isac10: "ac10",
            isautocannon10: "ac10",
            isac20: "ac20",
            isautocannon20: "ac20",
            islightgaussrifle: "lgauss",
            islightgauss: "lgauss",
            isgaussrifle: "gauss",
            isgauss: "gauss",
            isheavygaussrifle: "hgauss",
            isheavygauss: "hgauss",
            isimpheavygaussrifle: "ihgauss",
            isimpheavygauss: "ihgauss",
            isimprovedheavygaussrifle: "ihgauss",
            isimprovedheavygauss: "ihgauss",
            ismagshot: "magshot",
            ismagshotgr: "magshot",
            issbgr: "sbgauss",
            issilverbulletgauss: "sbgauss",
            issilverbulletgaussrifle: "sbgauss",
            ishvac2: "hvac2",
            ishypervelocityautocannon2: "hvac2",
            ishvac5: "hvac5",
            ishypervelocityautocannon5: "hvac5",
            ishvac10: "hvac10",
            ishypervelocityautocannon10: "hvac10",
            islb2xac: "lb2x",
            islb2x: "lb2x",
            islbxac2: "lb2x",
            islb5xac: "lb5x",
            islb5x: "lb5x",
            islbxac5: "lb5x",
            islb10xac: "lb10x",
            islb10x: "lb10x",
            islbxac10: "lb10x",
            islb20xac: "lb20x",
            islb20x: "lb20x",
            islbxac20: "lb20x",
            islac2: "lac2",
            islightac2: "lac2",
            islightautocannon2: "lac2",
            islac5: "lac5",
            islightac5: "lac5",
            islightautocannon5: "lac5",
            islightmachinegun: "lmg",
            islightmg: "lmg",
            ismachinegun: "mg",
            ismg: "mg",
            isheavymachinegun: "hmg",
            isheavymg: "hmg",
            isnailrivet: "nailrivet",
            isnailrivetgun: "nailrivet",
            isnailgun: "nailrivet",
            isrivetgun: "nailrivet",
            isrotaryac2: "rac2",
            isrotaryassaultcannon2: "rac2",
            isrotaryac5: "rac5",
            isrotaryassaultcannon5: "rac5",
            isultraac2: "uac2",
            isultraac5: "uac5",
            isultraac10: "uac10",
            isultraac20: "uac20",
            iserlargelaser: "erllas",
            isermediumlaser: "ermlas",
            isersmalllaser: "erslas",
            isflamer: "flamer",
            isvehicleflamer: "flamer",
            iserflamer: "erflamer",
            isheavyflamer: "hflamer",
            islargelaser: "llas",
            ismediumlaser: "mlas",
            issmalllaser: "slas",
            isplasmarifle: "plasrifle",
            islightppc: "lppc",
            islppc: "lppc",
            isppc: "ppc",
            isparticlecannon: "ppc",
            isheavyppc: "hppc",
            ishppc: "hppc",
            iserppc: "erppc",
            issnubnoseppc: "snppc",
            issnppc: "snppc",
            issnubnosedppc: "snppc",
            islargepulselaser: "lplas",
            ispulselargelaser: "lplas",
            ismediumpulselaser: "mplas",
            ispulsemedlaser: "mplas",
            issmallpulselaser: "splas",
            ispulsesmalllaser: "splas",
            islargexpulselaser: "lxplas",
            isxpulselargelaser: "lxplas",
            ismediumxpulselaser: "mxplas",
            isxpulsemedlaser: "mxplas",
            issmallxpulselaser: "sxplas",
            isxpulsesmalllaser: "sxplas",
            islargevsplaser: "vslplas",
            islvspl: "vslplas",
            islargevariablespeedlaser: "vslplas",
            islargevsp: "vslplas",
            ismediumvsplaser: "vsmplas",
            ismvspl: "vsmplas",
            ismediumvariablespeedlaser: "vsmplas",
            ismediumvsp: "vsmplas",
            issmallvsplaser: "vssplas",
            issvspl: "vssplas",
            issmallvariablespeedlaser: "vssplas",
            issmallvsp: "vssplas",
            islargereengineeredlaser: "rellas",
            islargerelaser: "rellas",
            ismediumreengineeredlaser: "remlas",
            ismediumrelaser: "remlas",
            issmallreengineeredlaser: "reslas",
            issmallrelaser: "reslas",
            isbinarylaserblazercannon: "blazer",
            isbinarylasercannon: "blazer",
            isblazer: "blazer",
            isbinarylaser: "blazer",
            isblazercannon: "blazer",
            islrm5: "lrm5",
            islrm10: "lrm10",
            islrm15: "lrm15",
            islrm20: "lrm20",
            islrt5: "lrt5",
            islrtorpedo5: "lrt5",
            islrt10: "lrt10",
            islrtorped10: "lrt10",
            islrt15: "lrt15",
            islrtorpedo15: "lrt15",
            islrt20: "lrt20",
            islrtorpedo20: "lrt20",
            isenhancedlrm5: "nlrm5",
            isenhancedlrm10: "nlrm10",
            isenhancedlrm15: "nlrm15",
            isenhancedlrm20: "nlrm20",
            isextendedlrm5: "elrm5",
            iselrm5: "elrm5",
            isextendedlrm10: "elrm10",
            iselrm10: "elrm10",
            isextendedlrm15: "elrm15",
            iselrm15: "elrm15",
            isextendedlrm20: "elrm20",
            iselrm20: "elrm20",
            ismml3: "mml3",
            ismml5: "mml5",
            ismml7: "mml7",
            ismml9: "mml9",
            ismrm10: "mrm10",
            ismrm20: "mrm20",
            ismrm30: "mrm30",
            ismrm40: "mrm40",
            isnarc: "narc",
            isnarcbeacon: "narc",
            isnarcmissilebeacon: "narc",
            isimprovednarc: "inarc",
            isinarcbeacon: "inarc",
            isinarcmissilebeacon: "inarc",
            isrocketlauncher10: "rl10",
            isrl10: "rl10",
            isrlauncher10: "rl10",
            isrocketlauncher15: "rl15",
            isrl15: "rl15",
            isrlauncher15: "rl15",
            isrocketlauncher20: "rl20",
            isrl20: "rl20",
            isrlauncher20: "rl20",
            issrm2: "srm2",
            issrm4: "srm4",
            issrm6: "srm6",
            issrt2: "srt2",
            issrtorpedo2: "srt2",
            issrt4: "srt4",
            issrtorpedo4: "srt4",
            issrt6: "srt6",
            issrtorpedo6: "srt6",
            isstreaksrm2: "ssrm2",
            isstreaksrm4: "ssrm4",
            isstreaksrm6: "ssrm6",
            isthunderbolt5: "tbolt5",
            isthunderbolt10: "tbolt10",
            isthunderbolt15: "tbolt15",
            isthunderbolt20: "tbolt20",
            isarrowiv: "arrowiv",
            isarrowivsystem: "arrowiv",
            isarrowivmissilesystem: "arrowiv",
            islongtom: "longtom",
            islongtomartillery: "longtom",
            islongtomcannon: "longtomcannon",
            islongtomartillerycannon: "longtomcannon",
            issniper: "sniper",
            issniperartillery: "sniper",
            issnipercannon: "snipercannon",
            issniperartillerycannon: "snipercannon",
            isthumper: "thumper",
            isthumperartillery: "thumper",
            isthumpercannon: "thumpercannon",
            isthumperartillerycannon: "thumpercannon",
            cllb2x: "clb2x",
            cllb2xac: "clb2x",
            cllbxac2: "clb2x",
            cllb5x: "clb5x",
            cllb5xac: "clb5x",
            cllbxac5: "clb5x",
            cllb10x: "clb10x",
            cllb10xac: "clb10x",
            cllbxac10: "clb10x",
            cllb20x: "clb20x",
            cllb20xac: "clb20x",
            cllbxac20: "clb20x",
            clapgaussrifle: "capgauss",
            clapgauss: "capgauss",
            clgaussrifle: "cgauss",
            clgauss: "cgauss",
            clhag20: "chag20",
            clhyperassaultgaussrifle20: "chag20",
            clhag30: "chag30",
            clhyperassaultgaussrifle30: "chag30",
            clhag40: "chag40",
            clhyperassaultgaussrifle40: "chag40",
            cllightmachinegun: "clmg",
            cllightmg: "clmg",
            clmachinegun: "cmg",
            clmg: "cmg",
            clheavymachinegun: "chmg",
            clheavymg: "chmg",
            clprotomechac2: "cpmac2",
            clprotomechac4: "cpmac4",
            clprotomechac8: "cpmac8",
            clnailrivet: "cnailrivet",
            clnailrivetgun: "cnailrivet",
            clnailgun: "cnailrivet",
            clrivetgun: "cnailrivet",
            clrotaryac2: "crac2",
            clrotaryassaultcannon2: "crac2",
            clrotaryac5: "crac5",
            clrotaryassaultcannon5: "crac5",
            clultraac2: "cuac2",
            clultraac5: "cuac5",
            clultraac10: "cuac10",
            clultraac20: "cuac20",
            clanultraac20: "cuac20",
            clerlargelaser: "cerllas",
            clermediumlaser: "cermlas",
            clersmalllaser: "cerslas",
            clermicrolaser: "cermiclas",
            clsmalllaser: "slas",
            clflamer: "cflamer",
            clvehicleflamer: "cflamer",
            clerflamer: "cerflamer",
            clheavyflamer: "chflamer",
            clheavylargelaser: "chllas",
            cllargeheavylaser: "chllas",
            clheavymediumlaser: "chmlas",
            clmediumheavylaser: "chmlas",
            clheavysmalllaser: "chslas",
            clsmallheavylaser: "chslas",
            climpheavylargelaser: "cihllas",
            climprovedheavylargelaser: "cihllas",
            climprovedlargeheavylaser: "cihllas",
            climpheavymediumlaser: "cihmlas",
            climprovedheavymediumlaser: "cihmlas",
            climprovedmediumheavylaser: "cihmlas",
            climpheavysmalllaser: "cihslas",
            climprovedheavysmalllaser: "cihslas",
            climprovedsmallheavylaser: "cihslas",
            clplasmacannon: "cplascannon",
            clerppc: "cerppc",
            cllargepulselaser: "clplas",
            clpulselargelaser: "clplas",
            clmediumpulselaser: "cmplas",
            clpulsemedlaser: "cmplas",
            clsmallpulselaser: "csplas",
            clpulsesmalllaser: "csplas",
            clmicropulselaser: "cmicplas",
            clerlargepulselaser: "cerlplas",
            clerpulselargelaser: "cerlplas",
            clermediumpulselaser: "cermplas",
            clerpulsemedlaser: "cermplas",
            clerpulsemediumlaser: "cermplas",
            clersmallpulselaser: "cersplas",
            clerpulsesmalllaser: "cersplas",
            cllargechemlaser: "cchemllas",
            cllargechemicallaser: "cchemllas",
            clmediumchemlaser: "cchemmlas",
            clmediumchemicallaser: "cchemmlas",
            clsmallchemlaser: "cchemslas",
            clsmallchemicallaser: "cchemslas",
            clatm3: "catm3",
            clatm6: "catm6",
            clatm9: "catm9",
            clatm12: "catm12",
            cliatm3: "ciatm3",
            cliatm6: "ciatm6",
            cliatm9: "ciatm9",
            cliatm12: "ciatm12",
            clnarc: "cnarc",
            clnarcbeacon: "cnarc",
            clnarcmissilebeacon: "cnarc",
            cllrm5: "clrm5",
            cllrm10: "clrm10",
            cllrm15: "clrm15",
            cllrm20: "clrm20",
            cllrt5: "clrt5",
            cllrtorpedo5: "clrt5",
            cllrt10: "clrt10",
            cllrtorpedo10: "clrt10",
            cllrt15: "clrt15",
            cllrtorpedo15: "clrt15",
            cllrt20: "clrt20",
            cllrtorpedo20: "clrt20",
            clstreaklrm5: "cslrm5",
            clstreaklrm10: "cslrm10",
            clstreaklrm15: "cslrm15",
            clstreaklrm20: "cslrm20",
            clsrm2: "csrm2",
            clsrm4: "csrm4",
            clsrm6: "csrm6",
            clsrt2: "csrt2",
            clsrtorpedo2: "srt2",
            clsrt4: "csrt4",
            clsrtorpedo4: "srt4",
            clsrt6: "csrt6",
            clsrtorpedo6: "srt6",
            clstreaksrm2: "cssrm2",
            clstreaksrm4: "cssrm4",
            clstreaksrm6: "cssrm6",
            clarrowiv: "carrowiv",
            clarrowivsystem: "carrowiv",
            clarrowivmissilesystem: "carrowiv",
            cllongtom: "longtom",
            cllongtomartillery: "longtom",
            cllongtomcannon: "longtomcannon",
            cllongtomartillerycannon: "longtomcannon",
            clsniper: "sniper",
            clsniperartillery: "sniper",
            clsnipercannon: "snipercannon",
            clsniperartillerycannon: "snipercannon",
            clthumper: "thumper",
            clthumperartillery: "thumper",
            clthumpercannon: "thumpercannon",
            clthumperartillerycannon: "thumpercannon",
            ishatchet: "hatchet",
            clhatchet: "hatchet",
            issword: "sword",
            clsword: "sword",
            ismace: "mace",
            clmace: "mace",
            isflail: "flail",
            clflail: "flail",
            isclaw: "claws",
            clclaw: "claws",
            islance: "lance",
            cllance: "lance",
            isbalightmachinegun: "lmg",
            isbalightmg: "lmg",
            isbamachinegun: "mg",
            isbamg: "mg",
            isbaheavymachinegun: "hmg",
            isbaheavymg: "hmg",
            isbafiredrakeneedler: "firedrake",
            isbafiredrakeincendiaryneedler: "firedrake",
            isbadavidlightgaussrifle: "david",
            isbakingdavidlightgaussrifle: "kdavid",
            isbagrandmaulergausscannon: "gmauler",
            isbagrandmauler: "gmauler",
            isbamagshot: "magshot",
            isbamagshotgr: "magshot",
            isbatsunamiheavygaussrifle: "tsunami",
            isbamicrogrenadelauncher: "mgrenade",
            isbagrenadelauncher: "hgrenade",
            isbaheavygrenadelauncher: "hgrenade",
            isbaheavygl: "hgrenade",
            isbaheavybagrenadelauncher: "hgrenade",
            isbaautogl: "hgrenade",
            isbalightmortar: "lmortar",
            isbaheavymortar: "hmortar",
            isbalightrecoillessrifle: "lrecoil",
            islightrecoillessrifle: "lrecoil",
            isbamediumrecoillessrifle: "mrecoil",
            ismediumrecoillessrifle: "mrecoil",
            isbaheavyrecoillessrifle: "hrecoil",
            isheavyrecoillessrifle: "hrecoil",
            isbamediumlaser: "mlas",
            isbasmalllaser: "slas",
            isbaermediumlaser: "ermlas",
            isbaersmalllaser: "erslas",
            isbamediumpulselaser: "mplas",
            isbapulsemedlaser: "mplas",
            isbasmallpulselaser: "splas",
            isbapulsesmalllaser: "splas",
            isbamediumvsplaser: "vsmplas",
            isbamvspl: "vsmplas",
            isbamediumvariablespeedlaser: "vsmplas",
            isbamediumvsp: "vsmplas",
            isbasmallvsplaser: "vssplas",
            isbasvspl: "vssplas",
            isbasmallvariablespeedlaser: "vssplas",
            isbasmallvsp: "vssplas",
            isbaflamer: "flamer",
            isbaheavyflamer: "hflamer",
            isbaplasmarifle: "mpplasrifle",
            isbasupportppc: "sppc",
            isbacompactnarc: "compactnarc",
            isbalrm1: "lrm1",
            isbalrm2: "lrm2",
            isbalrm3: "lrm3",
            isbalrm4: "lrm4",
            isbalrm5: "lrm5",
            isbamrm1: "mrm1",
            isbamrm2: "mrm2",
            isbamrm3: "mrm3",
            isbamrm4: "mrm4",
            isbamrm5: "mrm5",
            isbarl1: "rl1",
            isbarlauncher1: "rl1",
            isbarocketlauncher1: "rl1",
            isbarl2: "rl2",
            isbarlauncher2: "rl2",
            isbarocketlauncher2: "rl2",
            isbarl3: "rl3",
            isbarlauncher3: "rl3",
            isbarocketlauncher3: "rl3",
            isbarl4: "rl4",
            isbarlauncher4: "rl4",
            isbarocketlauncher4: "rl4",
            isbarl5: "rl5",
            isbarlauncher5: "rl5",
            isbarocketlauncher5: "rl5",
            isbasrm1: "srm1",
            isbasrm2: "srm2",
            isbasrm3: "srm3",
            isbasrm4: "srm4",
            isbasrm5: "srm5",
            isbasrm6: "srm6",
            isbaminelauncher: "popmine",
            isbataser: "taser",
            clbaapgaussrifle: "capgauss",
            clbaapgauss: "capgauss",
            clbalbx: "clbx",
            clbearhuntersuperheavyac: "bearhunt",
            clbabearhuntersuperheavyac: "bearhunt",
            clbamicrogrenadelauncher: "mgrenade",
            clbagrenadelauncher: "hgrenade",
            clbaheavygrenadelauncher: "hgrenade",
            clbaheavygl: "hgrenade",
            clbaheavybagrenadelauncher: "hgrenade",
            clbaautogl: "hgrenade",
            clbalightmortar: "lmortar",
            clbaheavymortar: "hmortar",
            clbalightrecoillessrifle: "lrecoil",
            cllightrecoillessrifle: "lrecoil",
            clbamediumrecoillessrifle: "mrecoil",
            clmediumrecoillessrifle: "mrecoil",
            clbaheavyrecoillessrifle: "hrecoil",
            clheavyrecoillessrifle: "hrecoil",
            clbalightmachinegun: "clmg",
            clbalightmg: "clmg",
            clbamachinegun: "cmg",
            clbamg: "cmg",
            clbaheavymachinegun: "chmg",
            clbaheavymg: "chmg",
            clbamediumpulselaser: "cmplas",
            clbapulsemedlaser: "cmplas",
            clbasmallpulselaser: "csplas",
            clbapulsesmalllaser: "csplas",
            clbamicropulselaser: "cmicplas",
            clbaermediumlaser: "cermlas",
            clbaersmalllaser: "cerslas",
            clbaermicrolaser: "cermiclas",
            clbasmalllaser: "slas",
            clbaermediumpulselaser: "cermplas",
            clbaerpulsemedlaser: "cermplas",
            clbaerpulsemediumlaser: "cermplas",
            clbaersmallpulselaser: "cersplas",
            clbaerpulsesmalllaser: "cersplas",
            clbaheavymediumlaser: "chmlas",
            clbamediumheavylaser: "chmlas",
            clbaheavysmalllaser: "chslas",
            clbasmallheavylaser: "chslas",
            clbaflamer: "cflamer",
            clbaheavyflamer: "chflamer",
            clbasupportppc: "csppc",
            clbacompactnarc: "compactnarc",
            clbalrm1: "clrm1",
            clbalrm2: "clrm2",
            clbalrm3: "clrm3",
            clbalrm4: "clrm4",
            clbalrm5: "clrm5",
            clbasrm1: "csrm1",
            clbasrm2: "csrm2",
            clbasrm3: "csrm3",
            clbasrm4: "csrm4",
            clbasrm5: "csrm5",
            clbasrm6: "csrm6",
            clbaadvancedsrm1: "casrm1",
            clbaadvancedsrm2: "casrm2",
            clbaadvancedsrm3: "casrm3",
            clbaadvancedsrm4: "casrm4",
            clbaadvancedsrm5: "casrm5",
            clbaadvancedsrm6: "casrm6",
            cladvancedsrm1: "casrm1",
            cladvancedsrm2: "casrm2",
            cladvancedsrm3: "casrm3",
            cladvancedsrm4: "casrm4",
            cladvancedsrm5: "casrm5",
            cladvancedsrm6: "casrm6",
            clbamicrobomb: "cbombrack"
        },
        Oa.EquipmentAlias = {
            isantipersonnelpod: "apod",
            clantipersonnelpod: "apod",
            isapod: "apod",
            clapod: "apod",
            isbpod: "bpod",
            clbpod: "bpod",
            ismpod: "mpod",
            clmpod: "mpod",
            isams: "ams",
            clams: "ams",
            isantimissilesystem: "ams",
            clantimissilesystem: "ams",
            clantimissilesys: "ams",
            cllaserantimissilesys: "lams",
            islaserams: "lams",
            cllaserams: "lams",
            islaserantimissilesystem: "lams",
            cllaserantimissilesystem: "lams",
            isartemisiv: "aiv",
            clartemisiv: "aiv",
            clartemisv: "av",
            isartemisv: "av",
            isapollo: "apollo",
            isaes: "aes",
            isbeagleactiveprobe: "probe",
            isbloodhoundactiveprobe: "bhprobe",
            clactiveprobe: "cprobe",
            islightprobe: "lprobe",
            islightactiveprobe: "lprobe",
            cllightprobe: "clprobe",
            cllightactiveprobe: "clprobe",
            isc3mastercomputer: "c3m",
            isc3masterunit: "c3m",
            isc3master: "c3m",
            isc3slavecomputer: "c3s",
            isc3slaveunit: "c3s",
            isc3slave: "c3s",
            isc3masterboosteddystemunit: "c3bm",
            isc3boostedsystemslave: "c3bs",
            isc3boostedsystemslaveunit: "c3bs",
            isc3iunit: "c3i",
            isimprovedc3cpu: "c3i",
            isc3icomputer: "c3i",
            iscase: "case",
            clcase: "case",
            iscaseii: "case2",
            clcaseii: "case2",
            isecm: "ecm",
            clecm: "cecm",
            isguardianecmsuite: "ecm",
            isguardianecm: "ecm",
            isecmsuite: "ecm",
            clecmsuite: "cecm",
            isangelecmsuite: "aecm",
            clangelecmsuite: "aecm",
            isangelecm: "aecm",
            clangelecm: "aecm",
            isjumpjet: "jump",
            cljumpjet: "jump",
            improvedjumpjet: "ijump",
            isimprovedjumpjet: "ijump",
            climprovedjumpjet: "ijump",
            ismasc: "masc",
            clmasc: "masc",
            istag: "tag",
            cltag: "tag",
            islighttag: "ltag",
            cllighttag: "ltag",
            istargetingcomputer: "tc",
            cltargetingcomputer: "tc",
            istsm: "tsm",
            cltsm: "tsm",
            istriplestrengthmyomer: "tsm",
            cltriplestrengthmyomer: "tsm",
            issupercharger: "supercharger",
            clsupercharger: "supercharger",
            clwatchdogecmsuite: "cews",
            heavydutygyro: "hdgyro",
            ispartialwing: "partwing",
            clpartialwing: "partwing",
            iscoolantpod: "cpod",
            clcoolantpod: "cpod",
            isppccapacitor: "ppccapacitor",
            clppccapacitor: "ppccapacitor",
            smallcockpit: "smcp",
            torsomountedcockpit: "tmcp",
            isumu: "umu",
            clumu: "umu",
            ismechanicaljumpbooster: "mechjumpbooster",
            clmechanicaljumpbooster: "mechjumpbooster",
            isquadturret: "turret",
            clquadturret: "turret",
            isheadturret: "turret",
            clheadturret: "turret",
            isshoulderturret: "turret",
            clshoulderturret: "turret",
            troopspace: "troopspace",
            TroopSpace: "troopspace",
            isbaturret: "turret",
            clbaturret: "turret",
            isdetachableweaponpack: "dwp",
            cldetachableweaponpack: "dwp",
            isbajumpbooster: "jumpbooster",
            clbajumpbooster: "jumpbooster",
            isbamechanicaljumpbooster: "jumpbooster",
            clbamechanicaljumpbooster: "jumpbooster",
            isbapartialwing: "partwing",
            clbapartialwing: "partwing",
            isbalprobe: "lprobe",
            clbalprobe: "lprobe",
            isbalighttag: "ltag",
            clbalighttag: "ltag",
            isbaapds: "apds",
            clbaapds: "apds",
            clbamyomerbooster: "myomerboost",
            clbamb: "myomerboost",
            isbaecm: "ecm",
            clbaecm: "cecm",
            isbaguardianecmsuite: "ecm",
            isbaguardianecm: "ecm",
            isbaecmsuite: "ecm",
            clbaecmsuite: "cecm",
            isbaangelecmsuite: "aecm",
            clbaangelecmsuite: "aecm",
            isbaangelecm: "aecm",
            clbaangelecm: "aecm",
            isbasinglehexecm: "ecm",
            clbasinglehexecm: "cecm",
            isbac3: "c3s",
            isbc3: "c3s",
            isbac3i: "c3i",
            isbc3i: "c3i"
        },
        Oa.LocationAlias = {
            "left arm": "LA",
            "right arm": "RA",
            "center torso": "T",
            "left torso": "T",
            "right torso": "T",
            head: "HD",
            "left leg": "LL",
            "right leg": "RL",
            "front left leg": "LFL",
            "front right leg": "RFL",
            "rear left leg": "LRL",
            "rear right leg": "RRL"
        };
        const Da = Oa;
        class Ua {
            static getCrit(e, a, t, n, s) {
                const r = e.indexOf("(r)") >= 0
                  , i = e.indexOf("(t)") >= 0;
                var l = e.indexOf("clan") >= 0
                  , o = e.indexOf("ammo") >= 0
                  , m = e.indexOf("(os)") >= 0 || e.indexOf("(ios)") >= 0 || e.indexOf("(i-os)") >= 0
                  , c = e.replace(/ *\([^)]*\) */g, "").replace(/[\W_]+/g, "");
                if (c.startsWith("bais") ? c = "isba" + c.substring(4) : c.startsWith("bacl") ? (c = "clba" + c.substring(4),
                l = !0) : c.startsWith("clanti") && (c = c.substring(2),
                l = !0),
                (c = c.replace("clan", "").replace("prototype", "").replace("primitive", "").replace("cluster", "").replace("slug", "").replace("homing", "").replace("clammofull", "").replace("clammohalf", "").replace("clammo", "").replace("ammofull", "").replace("ammohalf", "").replace("ammo", "").replace("full", "").replace("half", "").replace("narccapable", "").replace("artemiscapable", "").replace("artemisvcapable", "").replace("omni", "").replace("battlearmor", "ba")).endsWith("ios") ? (m = !0,
                c = c.substring(0, c.length - 3)) : c.endsWith("os") && (m = !0,
                c = c.substring(0, c.length - 2)),
                c.startsWith("is") || c.startsWith("cl") || (c = "Clan" === a.unit.tech || l ? "cl" + c : "is" + c),
                o)
                    this.getAmmo(c, a, t, s);
                else {
                    var u = Da.WeaponAlias[c];
                    if (u) {
                        r && (t = "(R) " + t),
                        i && (t = "TU");
                        var h = new y(a.unit,{
                            id: u,
                            location: t,
                            useOS: m
                        });
                        if (h.crits > 1 && a.unit.type !== A.UnitTypeEnum.BA) {
                            if (n.hasDebt(u, t))
                                return void n.credit(u, t, 1);
                            if (h.crits >= 8) {
                                var g = this.splitLocations(a.unit.motiveType, t);
                                for (let e = 0; e < g.length; e++)
                                    if (n.hasDebt(u, g[e]))
                                        return void n.credit(u, g[e], 1)
                            }
                            n.debit(u, t, h.crits - 1)
                        }
                        a.unit.addWeapon(h)
                    } else {
                        var p = Da.EquipmentAlias[c];
                        if (p) {
                            var x = new d({
                                id: p,
                                location: t
                            });
                            if (a.unit.hasEquipment(x)) {
                                if (x.isLimited) {
                                    a.unit.getEquipment(x).uses += 1
                                }
                            } else
                                x.isLimited && (x.uses = 1),
                                a.unit.addEquipment(x)
                        } else
                            ;
                    }
                }
            }
            static getAmmo(e, a, t, n) {
                e.startsWith("clatm") && (e.endsWith("he") || e.endsWith("er")) ? e = e.substring(0, e.length - 2) : e.startsWith("ismml") && (e.endsWith("lrm") || e.endsWith("srm")) && (e = e.substring(0, e.length - 3));
                const s = e => {
                    var a = e;
                    return e.startsWith("is") ? a = "cl" + e.substring(2) : e.startsWith("cl") && (a = "is" + e.substring(2)),
                    a
                }
                ;
                var r, i;
                if ((r = Da.WeaponAlias[e] || Da.WeaponAlias[s(e)]) || (i = Da.EquipmentAlias[e] || Da.EquipmentAlias[s(e)]),
                r || i) {
                    var l, o, m = r && (null === (l = g.Data[r]) || void 0 === l ? void 0 : l.useAmmo) || i && (null === (o = h.Data[i]) || void 0 === o ? void 0 : o.useAmmo);
                    if (m) {
                        var c = new d({
                            id: n ? "ammolimited" : "ammo",
                            location: t,
                            subtype: m,
                            uses: n
                        });
                        if (a.unit.hasEquipment(c)) {
                            if ("ammolimited" === c.id) {
                                a.unit.getEquipment(c).uses += n
                            }
                        } else
                            a.unit.addEquipment(c)
                    }
                } else
                    a.errors += "Error: Unable to match Weapon/Equipment for Ammo: " + e + ".\n"
            }
            static splitLocations(e, a) {
                return e === L.MotiveTypeEnum.BP && "T" === a ? ["RA", "LA"] : e === L.MotiveTypeEnum.QD && "T" === a ? ["fRL", "fLL", "rRL", "rLL"] : []
            }
        }
        function Ha() {
            return this.ledger = {},
            {
                hasDebt: (e, a) => !!(this.ledger[e] && this.ledger[e][a] > 0),
                credit: (e, a, t) => {
                    this.ledger[e][a] -= t
                }
                ,
                debit: (e, a, t) => {
                    this.ledger[e] || (this.ledger[e] = {}),
                    this.ledger[e][a] ? this.ledger[e][a] += t : this.ledger[e][a] = t
                }
            }
        }
        const Va = class {
            static import(e) {
                try {
                    const r = e.split("\n")
                      , i = new Ha;
                    var a, t, n, s = {
                        unit: new L,
                        errors: ""
                    };
                    for (let e = 0; e < r.length; e++) {
                        let l = r[e];
                        if (l = l.trim(),
                        "-Empty-" !== l)
                            if ("" !== l)
                                if (0 !== e)
                                    if (1 !== e)
                                        if (2 !== e)
                                            l = l.toLowerCase(),
                                            l.startsWith("clanname:") ? s.unit.clanname = r[e].trim().substring(9) : l.startsWith("chassis:") ? this.getChassis(l.substring(8), s) : l.startsWith("model:") ? this.getVariant(l.substring(6), s) : l.startsWith("config:") ? this.getType(l.substring(7), s) : l.startsWith("techbase:") ? this.getTech(l.substring(9), s) : l.startsWith("motive:") ? this.getMotive(l.substring(7), s) : l.startsWith("mass:") ? this.getTonnage(l.substring(5), s) : l.startsWith("cockpit:") ? this.getCockpit(l.substring(8), s) : l.startsWith("gyro:") ? this.getGyro(l.substring(5), s) : l.startsWith("ejection:") ? this.getEjectionSystem(l.substring(9), s) : l.startsWith("engine:") ? this.getEngine(l.substring(7), s) : l.startsWith("structure:") ? this.getStructureType(l.substring(10), s) : l.startsWith("heat sinks:") ? this.getSinks(l.substring(11), s) : l.startsWith("walk mp:") ? this.getWalk(l.substring(8), s) : l.startsWith("jump mp:") ? this.getJump(l.substring(8), s) : l.startsWith("armor:") ? (this.getArmorType(l.substring(6), s),
                                            a = !0) : a ? this.getArmor(l, s) : Da.LocationAlias[l.replace(":", "")] ? (t = !0,
                                            n = Da.LocationAlias[l.replace(":", "")]) : t && Ua.getCrit(l, s, n, i);
                                        else {
                                            if (l.startsWith("mul id:"))
                                                continue;
                                            if (l.toLowerCase().startsWith("clanname:")) {
                                                s.unit.clanname = l.substring(9);
                                                continue
                                            }
                                            if (l.toLowerCase().startsWith("model:")) {
                                                this.getVariant(l.substring(6), s);
                                                continue
                                            }
                                            this.getVariant(l, s)
                                        }
                                    else {
                                        if (l.startsWith("model:")) {
                                            this.getVariant(l.substring(6), s);
                                            continue
                                        }
                                        if (l.toLowerCase().startsWith("clanname:")) {
                                            s.unit.clanname = l.substring(9);
                                            continue
                                        }
                                        if (l.toLowerCase().startsWith("chassis:")) {
                                            this.getChassis(l.substring(8), s);
                                            continue
                                        }
                                        this.getChassis(l, s)
                                    }
                                else {
                                    if (l.startsWith("chassis:")) {
                                        this.getChassis(l.substring(8), s);
                                        continue
                                    }
                                    this.getVersion(l, s)
                                }
                            else
                                a = !1,
                                t = !1
                    }
                } catch (r) {
                    throw console.log(r),
                    s.errors += "Unexpected Error: " + r,
                    r
                }
                return s
            }
            static getVersion(e, a) {
                Number(e.substring(8).trim())
            }
            static getChassis(e, a) {
                e ? a.unit.chassis = e : a.errors += "Error: Unable to import Chassis name for: " + e + ".\n"
            }
            static getVariant(e, a) {
                e ? a.unit.variant = e : a.errors += "Error: Unable to import Variant name for: " + e + ".\n"
            }
            static getType(e, a) {
                e.indexOf("omni") >= 0 && (a.unit.isOmni = !0),
                e.indexOf("quadvee") >= 0 ? a.unit.type = "cv" : e.indexOf("biped") >= 0 || e.indexOf("quad") >= 0 ? (a.unit.type = A.UnitTypeEnum.BM,
                a.unit.motiveType = e.indexOf("quad") >= 0 ? L.MotiveTypeEnum.QD : L.MotiveTypeEnum.BP) : a.errors += "Error: Unable to import Unit Type for: " + e + ".\n"
            }
            static getMotive(e, a) {
                e.indexOf("track") >= 0 ? a.unit.motive = "Tracked" : e.indexOf("wheel") >= 0 ? a.unit.motive = "Wheeled" : e.indexOf("hover") >= 0 ? a.unit.motive = "Hover" : e.indexOf("vtol") >= 0 ? a.unit.motive = "VTOL" : a.errors += "Error: Unable to import Motive Type for: " + e + ".\n"
            }
            static getTech(e, a) {
                e.indexOf("mixed") >= 0 ? a.unit.tech = A.TechEnum.Mixed : e.indexOf("inner sphere") >= 0 ? a.unit.tech = A.TechEnum.IS : e.indexOf("clan") >= 0 ? (a.unit.tech = A.TechEnum.Clan,
                a.unit.addEquipment(new d({
                    id: "freecase"
                }))) : a.errors += "Error: Unable to import Tech for: " + e + ".\n"
            }
            static getTonnage(e, a) {
                const t = parseInt(e);
                isNaN(t) ? a.errors += "Error: Unable to import Tonnage for: " + e + ".\n" : a.unit.tonnage = t
            }
            static getCockpit(e, a) {
                var t = e.replace(/ *\([^)]*\) */g, "").replace(/[\W_]+/g, "").toLowerCase();
                if (t in Da.EquipmentAlias && !a.unit.isEquipedWith(t)) {
                    var n = new d({
                        id: Da.EquipmentAlias[t]
                    });
                    a.unit.addEquipment(n)
                }
            }
            static getGyro(e, a) {
                var t = e.replace(/ *\([^)]*\) */g, "").replace(/[\W_]+/g, "").toLowerCase();
                if (t in Da.EquipmentAlias && !a.unit.isEquipedWith(t)) {
                    var n = new d({
                        id: Da.EquipmentAlias[t]
                    });
                    a.unit.addEquipment(n)
                }
            }
            static getEjectionSystem(e, a) {
                var t = e.replace(/ *\([^)]*\) */g, "").replace(/[\W_]+/g, "").toLowerCase();
                if (t in Da.EquipmentAlias && !a.unit.isEquipedWith(t)) {
                    var n = new d({
                        id: Da.EquipmentAlias[t]
                    });
                    a.unit.addEquipment(n)
                }
            }
            static getWalk(e, a) {
                const t = parseInt(e);
                isNaN(t) ? a.errors += "Error: Unable to import Walk MP for: " + e + ".\n" : a.unit.walk = t
            }
            static getJump(e, a) {
                const t = parseInt(e);
                isNaN(t) ? a.errors += "Error: Unable to import Jump MP for: " + e + ".\n" : a.unit.jump = t
            }
            static getSinks(e, a) {
                var t = parseInt(e);
                isNaN(t) ? a.errors += "Error: Unable to import Heat Dissipation for: " + e + ".\n" : (a.unit.sinks = t,
                a.unit.hasDHS = e.indexOf("double") >= 0)
            }
            static getEngine(e, a) {
                if (e.replace(/\s/g, "").indexOf("lightengine") >= 0)
                    a.unit.addEquipment(new d({
                        id: "lfe"
                    }));
                else {
                    var t = "xle";
                    e.indexOf("xxl") >= 0 && (t = "xxle"),
                    e.indexOf("xl") >= 0 && (e.indexOf("clan") >= 0 ? a.unit.addEquipment(new d({
                        id: "c" + t
                    })) : a.unit.addEquipment(new d({
                        id: t
                    })))
                }
            }
            static getArmor(e, a) {
                const t = e.split(":");
                if (t.length < 2)
                    return;
                const n = t[0].replace(/[\W_]+/g, "")
                  , s = parseInt(t[1].trim())
                  , r = Da.ArmorAlias[n];
                isNaN(s) ? a.errors += "Error: Unable to import Armor value for: " + e + ".\n" : r ? a.unit.armor[r] = s : a.errors += "Error: Unable to import Armor location for: " + e + ".\n"
            }
            static getArmorType(e, a) {
                var t = e.replace(/ *\([^)]*\) */g, "").replace(/[\W_]+/g, "").replace(" ", "").toLowerCase();
                if (t in Da.ArmorTypeAlias && !a.unit.isEquipedWith(t)) {
                    var n = new d({
                        id: Da.ArmorTypeAlias[t]
                    });
                    a.unit.addEquipment(n)
                }
            }
            static getStructureType(e, a) {
                var t = e.replace(/ *\([^)]*\) */g, "").replace(/[\W_]+/g, "").toLowerCase();
                if (0 === t.indexOf("clan") && (a.unit.isEquipedWith("freecase") || a.unit.addEquipment(new d({
                    id: "freecase"
                }))),
                t in Da.StructureTypeAlias && !a.unit.isEquipedWith(t)) {
                    var n = new d({
                        id: Da.StructureTypeAlias[t]
                    });
                    a.unit.addEquipment(n)
                }
            }
        }
        ;
        class Ja {
            static import(e) {
                var a, t;
                const n = ("<blk>\n" + e + "\n</blk>").replace(/<\/?.+>/gi, e => e.replace(/\s/g, "_").toLowerCase())
                  , s = (new DOMParser).parseFromString(n, "application/xml")
                  , r = null === (a = s.querySelector("unittype")) || void 0 === a || null === (t = a.textContent) || void 0 === t ? void 0 : t.trim().toLowerCase();
                var i;
                return "battlearmor" === r ? (i = {
                    unit: new D,
                    errors: ""
                },
                this.import_BA(i, s)) : ["aero", "convfighter"].includes(r) ? (i = {
                    unit: new K,
                    errors: ""
                },
                this.importFighter(i, r, s)) : (i = {
                    unit: new X,
                    errors: ""
                },
                this.import_CV(i, s)),
                i
            }
            static importFighter(e, a, t) {
                var n, s, r, i, l, o, m, c, u, h, d, g, p, y, x, v, M, L, f, S, b, C, T, R, j, w, E, B, P, k, I, F, q, X, N, W;
                e.unit.tonnage = null === (n = t.querySelector("tonnage")) || void 0 === n || null === (s = n.textContent) || void 0 === s ? void 0 : s.trim(),
                e.unit.chassis = null === (r = t.querySelector("name")) || void 0 === r || null === (i = r.textContent) || void 0 === i ? void 0 : i.trim(),
                e.unit.variant = null === (l = t.querySelector("model")) || void 0 === l || null === (o = l.textContent) || void 0 === o ? void 0 : o.trim(),
                e.unit.tech = A.TechEnum[null === (m = t.querySelector("type")) || void 0 === m || null === (c = m.textContent) || void 0 === c || null === (u = c.trim()) || void 0 === u || null === (h = u.split(" ")) || void 0 === h ? void 0 : h[0]],
                e.unit.motiveType = "aero" === a ? K.MotiveTypeEnum.ASF : K.MotiveTypeEnum.CF,
                e.unit.thrust = null === (d = t.querySelector("safethrust")) || void 0 === d || null === (g = d.textContent) || void 0 === g ? void 0 : g.trim(),
                e.unit.sinks = null === (p = t.querySelector("heatsinks")) || void 0 === p || null === (y = p.textContent) || void 0 === y ? void 0 : y.trim(),
                e.unit.hasDHS = "1" === (null === (x = t.querySelector("sink_type")) || void 0 === x || null === (v = x.textContent) || void 0 === v ? void 0 : v.trim()),
                e.unit.isOmni = "1" === (null === (M = t.querySelector("omni")) || void 0 === M || null === (L = M.textContent) || void 0 === L ? void 0 : L.trim());
                let z = null === (f = t.querySelector("armor")) || void 0 === f || null === (S = f.textContent) || void 0 === S || null === (b = S.trim()) || void 0 === b ? void 0 : b.split("\n");
                this.parse_fighter_armor(e.unit, z),
                this.parse_equipment(e, K.LocationEnum.N, null === (C = t.querySelector("nose_equipment")) || void 0 === C || null === (T = C.textContent) || void 0 === T || null === (R = T.trim()) || void 0 === R ? void 0 : R.split("\n")),
                this.parse_equipment(e, K.LocationEnum.LW, null === (j = t.querySelector("left_wing_equipment")) || void 0 === j || null === (w = j.textContent) || void 0 === w || null === (E = w.trim()) || void 0 === E ? void 0 : E.split("\n")),
                this.parse_equipment(e, K.LocationEnum.RW, null === (B = t.querySelector("right_wing_equipment")) || void 0 === B || null === (P = B.textContent) || void 0 === P || null === (k = P.trim()) || void 0 === k ? void 0 : k.split("\n")),
                this.parse_equipment(e, K.LocationEnum.A, null === (I = t.querySelector("aft_equipment")) || void 0 === I || null === (F = I.textContent) || void 0 === F || null === (q = F.trim()) || void 0 === q ? void 0 : q.split("\n")),
                this.parse_equipment(e, K.LocationEnum.FU, null === (X = t.querySelector("fuselage_equipment")) || void 0 === X || null === (N = X.textContent) || void 0 === N || null === (W = N.trim()) || void 0 === W ? void 0 : W.split("\n"))
            }
            static import_CV(e, a) {
                var t, n, s, r, i, l, o, m, c, u, h, d, g, p, y, x, v, M, L, f, S, b, C, T, R, j, w, E, B, P, k, I, F, q, N, W, z, G, O, D, U, H, V, J, Q;
                e.unit.chassis = null === (t = a.querySelector("name")) || void 0 === t || null === (n = t.textContent) || void 0 === n ? void 0 : n.trim(),
                e.unit.variant = null === (s = a.querySelector("model")) || void 0 === s || null === (r = s.textContent) || void 0 === r ? void 0 : r.trim(),
                e.unit.motiveType = null === (i = a.querySelector("motion_type")) || void 0 === i || null === (l = i.textContent) || void 0 === l ? void 0 : l.trim(),
                e.unit.tonnage = null === (o = a.querySelector("tonnage")) || void 0 === o || null === (m = o.textContent) || void 0 === m ? void 0 : m.trim(),
                e.unit.tech = A.TechEnum[null === (c = a.querySelector("type")) || void 0 === c || null === (u = c.textContent) || void 0 === u || null === (h = u.trim()) || void 0 === h || null === (d = h.split(" ")) || void 0 === d ? void 0 : d[0]],
                e.unit.cruise = null === (g = a.querySelector("cruisemp")) || void 0 === g || null === (p = g.textContent) || void 0 === p ? void 0 : p.trim(),
                e.unit.isOmni = "1" === (null === (y = a.querySelector("omni")) || void 0 === y || null === (x = y.textContent) || void 0 === x ? void 0 : x.trim()) || !1;
                let _ = null === (v = a.querySelector("armor")) || void 0 === v || null === (M = v.textContent) || void 0 === M || null === (L = M.trim()) || void 0 === L ? void 0 : L.split("\n");
                e.unit.hasTurret = (null === _ || void 0 === _ ? void 0 : _.length) > 4 && e.unit.motiveType !== X.MotiveTypeEnum.V,
                this.parse_armor(e.unit, _),
                this.getArmorType(null === (f = a.querySelector("armor_type")) || void 0 === f || null === (S = f.textContent) || void 0 === S ? void 0 : S.trim(), e),
                this.parse_equipment(e, X.LocationsEnum.BD, null === (b = a.querySelector("body_equipment")) || void 0 === b || null === (C = b.textContent) || void 0 === C || null === (T = C.trim()) || void 0 === T ? void 0 : T.split("\n")),
                this.parse_equipment(e, X.LocationsEnum.FR, null === (R = a.querySelector("front_equipment")) || void 0 === R || null === (j = R.textContent) || void 0 === j || null === (w = j.trim()) || void 0 === w ? void 0 : w.split("\n")),
                this.parse_equipment(e, X.LocationsEnum.LS, null === (E = a.querySelector("left_equipment")) || void 0 === E || null === (B = E.textContent) || void 0 === B || null === (P = B.trim()) || void 0 === P ? void 0 : P.split("\n")),
                this.parse_equipment(e, X.LocationsEnum.RS, null === (k = a.querySelector("right_equipment")) || void 0 === k || null === (I = k.textContent) || void 0 === I || null === (F = I.trim()) || void 0 === F ? void 0 : F.split("\n")),
                this.parse_equipment(e, X.LocationsEnum.RR, null === (q = a.querySelector("rear_equipment")) || void 0 === q || null === (N = q.textContent) || void 0 === N || null === (W = N.trim()) || void 0 === W ? void 0 : W.split("\n")),
                this.parse_equipment(e, X.LocationsEnum.TU, null === (z = a.querySelector("turret_equipment")) || void 0 === z || null === (G = z.textContent) || void 0 === G || null === (O = G.trim()) || void 0 === O ? void 0 : O.split("\n")),
                this.parse_equipment(e, X.LocationsEnum.RO, null === (D = a.querySelector("rotor_equipment")) || void 0 === D || null === (U = D.textContent) || void 0 === U || null === (H = U.trim()) || void 0 === H ? void 0 : H.split("\n")),
                this.get_transporters(e, null === (V = a.querySelector("transporters")) || void 0 === V || null === (J = V.textContent) || void 0 === J || null === (Q = J.trim()) || void 0 === Q ? void 0 : Q.split("\n"))
            }
            static import_BA(e, a) {
                var t, n, s, r, i, l, o, m, c, u, h, d, g, p, y, x, v, M, L, f, S, b, C, T, R, j, w, E, B, P;
                e.unit.chassis = null === (t = a.querySelector("name")) || void 0 === t || null === (n = t.textContent) || void 0 === n ? void 0 : n.trim(),
                e.unit.variant = null === (s = a.querySelector("model")) || void 0 === s || null === (r = s.textContent) || void 0 === r ? void 0 : r.trim(),
                e.unit.motiveType = function(e) {
                    var a;
                    return (null === e || void 0 === e || null === (a = e.charAt(0)) || void 0 === a ? void 0 : a.toUpperCase()) + (null === e || void 0 === e ? void 0 : e.slice(1))
                }(null === (i = a.querySelector("chassis")) || void 0 === i || null === (l = i.textContent) || void 0 === l ? void 0 : l.trim()),
                e.unit.weightClass = this.getWeightClass(null === (o = a.querySelector("weightclass")) || void 0 === o || null === (m = o.textContent) || void 0 === m ? void 0 : m.trim()),
                e.unit.tech = A.TechEnum[null === (c = a.querySelector("type")) || void 0 === c || null === (u = c.textContent) || void 0 === u || null === (h = u.trim()) || void 0 === h || null === (d = h.split(" ")) || void 0 === d ? void 0 : d[0]],
                e.unit.squadSize = null === (g = a.querySelector("trooper_count")) || void 0 === g || null === (p = g.textContent) || void 0 === p ? void 0 : p.trim(),
                e.unit.groundMP = null === (y = a.querySelector("cruisemp")) || void 0 === y || null === (x = y.textContent) || void 0 === x ? void 0 : x.trim(),
                e.unit.otherMotiveType = D.OtherMotiveTypeEnum[null === (v = a.querySelector("motion_type")) || void 0 === v || null === (M = v.textContent) || void 0 === M ? void 0 : M.trim()] || "",
                e.unit.otherMP = null === (L = a.querySelector("jumpingmp")) || void 0 === L || null === (f = L.textContent) || void 0 === f ? void 0 : f.trim(),
                e.unit.armor = {
                    Body: null === (S = a.querySelector("armor")) || void 0 === S || null === (b = S.textContent) || void 0 === b ? void 0 : b.trim()
                },
                a.querySelector("turret") && this.parse_equipment_BA(e, ["turret"]),
                this.getArmorType(null === (C = a.querySelector("armor_type")) || void 0 === C || null === (T = C.textContent) || void 0 === T ? void 0 : T.trim(), e),
                this.parse_equipment_BA(e, (null === (R = a.querySelector("squad_equipment")) || void 0 === R || null === (j = R.textContent) || void 0 === j || null === (w = j.trim()) || void 0 === w ? void 0 : w.split("\n")) || (null === (E = a.querySelector("point_equipment")) || void 0 === E || null === (B = E.textContent) || void 0 === B || null === (P = B.trim()) || void 0 === P ? void 0 : P.split("\n")))
            }
            static parse_armor(e, a) {
                null !== a && void 0 !== a && a.length && (e.armor[X.LocationsEnum.FR] = +a[0],
                e.armor[X.LocationsEnum.LS] = +a[1],
                e.armor[X.LocationsEnum.RS] = +a[2],
                e.armor[X.LocationsEnum.RR] = +a[3],
                a.length > 4 && (e.hasTurret && (e.armor[X.LocationsEnum.TU] = +a[4]),
                e.motiveType === X.MotiveTypeEnum.V && (e.armor[X.LocationsEnum.RO] = +a[4])))
            }
            static parse_fighter_armor(e, a) {
                null !== a && void 0 !== a && a.length && (e.armor[K.ArmorLocationEnum.N] = +a[0],
                e.armor[K.ArmorLocationEnum.LW] = +a[1],
                e.armor[K.ArmorLocationEnum.RW] = +a[2],
                e.armor[K.ArmorLocationEnum.A] = +a[3])
            }
            static parse_equipment(e, a, t) {
                let n = new Qa;
                null === t || void 0 === t || t.forEach(t => {
                    t && Ua.getCrit(t.trim().toLowerCase(), e, a, n)
                }
                )
            }
            static parse_equipment_BA(e, a) {
                let t = new Qa;
                null === a || void 0 === a || a.forEach(a => {
                    if (a) {
                        var n, s = a.split(":"), r = s[0].trim().toLowerCase(), i = D.LocationsEnum.Body;
                        if (s[1]) {
                            var l = s[1].trim().toLowerCase();
                            ["la", "ra"].includes(l) && (i = D.LocationsEnum.Arm),
                            "tu" === l && e.unit.isEquipedWith("turret") && (i = D.LocationsEnum.TU),
                            "dwp" === l && e.unit.isEquipedWith("dwp") && (i = D.LocationsEnum.DWP)
                        }
                        if (s[2]) {
                            var o = s[2].trim().toLowerCase();
                            o.indexOf("shots") >= 0 && (o = o.replace("shots", "").replace("#", ""),
                            n = parseInt(o))
                        }
                        Ua.getCrit(r, e, i, t, n)
                    }
                }
                )
            }
            static get_transporters(e, a) {
                null === a || void 0 === a || a.forEach(a => {
                    let t = a.split(":");
                    if (2 === t.length) {
                        let a = t[0]
                          , s = parseFloat(t[1])
                          , r = Da.EquipmentAlias[a];
                        if (r) {
                            var n = new d({
                                id: r
                            });
                            n.uses = s,
                            e.unit.hasEquipment(n) || e.unit.addEquipment(n)
                        }
                    } else
                        console.log("Invalid transporter value: '", a, "'")
                }
                )
            }
            static getArmorType(e, a) {
                let t = (e => {
                    switch (+e) {
                    case 2:
                        return "reactive";
                    case 3:
                        return "lasrefl";
                    case 4:
                        return "hardened";
                    case 16:
                        return "ferolam";
                    case 22:
                        return "stealth";
                    case 31:
                    case 32:
                    case 33:
                    case 34:
                        return "bastealth";
                    case 35:
                        return "bafireresist";
                    case 36:
                        return "bamimetic";
                    case 37:
                        return "bareflective";
                    case 38:
                        return "bareactive";
                    default:
                        return !1
                    }
                }
                )(+e);
                if (t && !a.unit.isEquipedWith(t)) {
                    var n = new d({
                        id: t
                    });
                    a.unit.addEquipment(n)
                }
            }
            static getWeightClass(e) {
                return (e => {
                    switch (+e) {
                    case 0:
                        return D.WeightClassEnum.PAL;
                    case 1:
                        return D.WeightClassEnum.Light;
                    case 2:
                        return D.WeightClassEnum.Medium;
                    case 3:
                        return D.WeightClassEnum.Heavy;
                    case 4:
                        return D.WeightClassEnum.Assault;
                    default:
                        return !1
                    }
                }
                )(+e)
            }
        }
        function Qa() {
            return {
                hasDebt: (e, a) => !1,
                credit: (e, a, t) => {}
                ,
                debit: (e, a, t) => {}
            }
        }
        class _a extends n.Component {
            constructor(e) {
                super(e),
                this.state = {
                    file: null,
                    error: null,
                    log: "",
                    imported: null,
                    progress: null
                },
                this.type = null,
                this.fileInput = n.createRef(),
                this.handleHide = this.handleHide.bind(this),
                this.handleFileChange = this.handleFileChange.bind(this),
                this.handleFileImport = this.handleFileImport.bind(this)
            }
            render() {
                var e = !this.state.file || this.state.error || this.state.imported;
                return (0,
                b.jsxs)(oe.A, {
                    show: !0,
                    onHide: this.handleHide,
                    centered: !0,
                    scrollable: !0,
                    children: [(0,
                    b.jsxs)(oe.A.Header, {
                        className: "bg-gray-dark border-0",
                        children: ["Import data from an .MTF file", (0,
                        b.jsx)(i.A, {
                            onClick: this.handleHide,
                            size: "sm",
                            children: (0,
                            b.jsx)(S.hvQ, {})
                        })]
                    }), (0,
                    b.jsx)(oe.A.Body, {
                        className: "bg-gray-dark",
                        children: (0,
                        b.jsxs)(r.A, {
                            children: [(0,
                            b.jsx)(r.A.Row, {
                                children: (0,
                                b.jsx)(r.A.Group, {
                                    as: s.A,
                                    children: (0,
                                    b.jsxs)(r.A.File, {
                                        id: "file",
                                        custom: !0,
                                        children: [(0,
                                        b.jsx)(r.A.File.Input, {
                                            ref: this.fileInput,
                                            accept: ".mtf,.blk",
                                            onChange: this.handleFileChange,
                                            isInvalid: !!this.state.error
                                        }), (0,
                                        b.jsx)(r.A.File.Label, {
                                            children: this.state.file && this.state.file.name || "Choose file"
                                        }), (0,
                                        b.jsx)(r.A.Control.Feedback, {
                                            type: "invalid",
                                            children: this.state.error
                                        })]
                                    })
                                })
                            }), (0,
                            b.jsxs)(r.A.Row, {
                                children: [(0,
                                b.jsx)(r.A.Group, {
                                    as: s.A,
                                    xs: "auto",
                                    className: "my-auto",
                                    children: (0,
                                    b.jsx)(i.A, {
                                        disabled: e,
                                        onClick: this.handleFileImport,
                                        children: "Import"
                                    })
                                }), (0,
                                b.jsx)(r.A.Group, {
                                    as: s.A,
                                    controlId: "progress",
                                    className: "my-auto",
                                    children: this.state.progress ? (0,
                                    b.jsx)(Ga.A, {
                                        variant: "success",
                                        now: this.state.progress
                                    }) : null
                                })]
                            }), this.state.log ? (0,
                            b.jsx)(r.A.Row, {
                                children: (0,
                                b.jsx)(r.A.Group, {
                                    as: s.A,
                                    "aria-label": "Import Log",
                                    children: (0,
                                    b.jsx)(r.A.Text, {
                                        className: "mt-3 text-danger",
                                        children: this.state.log
                                    })
                                })
                            }) : null]
                        })
                    })]
                })
            }
            handleHide() {
                this.props.onHide(!1)
            }
            handleFileChange(e) {
                const a = e.target
                  , t = a.files[0];
                if (!t || !t.name)
                    return a.value = null,
                    void this.setState({
                        file: null,
                        error: "Invalid file type, expecting .mtf extension.",
                        log: "",
                        imported: null,
                        progress: null
                    });
                {
                    const e = t.name.slice((t.name.lastIndexOf(".") - 1 >>> 0) + 2).toLowerCase();
                    if (!["mtf", "blk"].includes(e))
                        return a.value = null,
                        void this.setState({
                            file: null,
                            error: "Invalid file type, expecting .mtf or .blk extension.",
                            log: "",
                            imported: null,
                            progress: null
                        });
                    this.type = e
                }
                this.setState({
                    file: t,
                    error: null,
                    log: "",
                    imported: null,
                    progress: null
                })
            }
            handleFileImport() {
                if (!this.state.file)
                    return;
                const e = new FileReader;
                e.addEventListener("load", e => {
                    const a = e.target.result
                      , t = ( () => {
                        switch (this.type) {
                        case "mtf":
                            return Va;
                        case "blk":
                            return Ja;
                        default:
                            return
                        }
                    }
                    )().import(a);
                    this.fileInput.current && (this.fileInput.current.value = null),
                    this.setState({
                        file: null,
                        imported: !0,
                        log: t.errors,
                        progress: 100
                    });
                    var n = t.unit;
                    this.props.onImport(n),
                    0 === t.errors.length && this.handleHide()
                }
                ),
                e.addEventListener("progress", e => {
                    if (e.loaded && e.total) {
                        const a = e.loaded / e.total * 50;
                        this.setState({
                            progress: Math.round(a)
                        })
                    }
                }
                ),
                e.readAsText(this.state.file)
            }
        }
        const Ka = _a
          , Ya = 2100
          , Za = 1500;
        class $a extends n.Component {
            constructor(e) {
                super(e),
                this.getDestiny = () => null != localStorage.getItem("destiny") && localStorage.getItem("destiny").includes('"isDestinyEnabled":true'),
                this.getDestinyInverse = () => 1 != this.getDestiny(),
                this.fontDetection = () => {
                    const e = ["falcon-regular", "falcon-bold", "vegas-regular"]
                      , a = "BESbswy";
                    var t = this.state.isFontsLoaded
                      , n = document.createElement("canvas").getContext("2d")
                      , s = new Array(e.length);
                    e.forEach( (e, t) => {
                        n.font = "normal 20px " + e;
                        const r = n.measureText(a);
                        s[t] = r.width
                    }
                    ),
                    function r(i, l) {
                        if (void 0 === l && (l = 0),
                        l >= 20)
                            i();
                        else if (t)
                            i();
                        else {
                            var o = 0;
                            e.forEach( (e, t) => {
                                n.font = "normal 20px " + e;
                                n.measureText(a).width !== s[t] && o++
                            }
                            ),
                            o === e.length ? (t = !0,
                            i()) : setTimeout(function() {
                                r(i, l + 1)
                            }, 1e3)
                        }
                    }( () => {
                        this.setState(e => ({
                            isFontsLoaded: !0
                        }))
                    }
                    )
                }
                ,
                this.state = {
                    pilot: new le,
                    unit: new L,
                    showImport: !1,
                    isFontsLoaded: !1
                },
                this.stageRef = n.createRef(),
                this.handleChangePilot = this.handleChangePilot.bind(this),
                this.handleResetPilot = this.handleResetPilot.bind(this),
                this.handleChangeUnit = this.handleChangeUnit.bind(this),
                this.handleAddUnitItem = this.handleAddUnitItem.bind(this),
                this.handleRemoveUnitItem = this.handleRemoveUnitItem.bind(this),
                this.handleChangeUnitItem = this.handleChangeUnitItem.bind(this),
                this.handleSortUnitItems = this.handleSortUnitItems.bind(this),
                this.handleGroupUnitWeapons = this.handleGroupUnitWeapons.bind(this),
                this.handleClearUnitItems = this.handleClearUnitItems.bind(this),
                this.handleResetUnit = this.handleResetUnit.bind(this),
                this.handleCardDownload = this.handleCardDownload.bind(this),
                this.handleShowImport = this.handleShowImport.bind(this),
                this.handleImport = this.handleImport.bind(this)
            }
            render() {
                const e = this.state.unit.clone()
                  , a = e.validate()
                  , t = this.state.pilot.clone()
                  , n = tt(e, t)
                  , m = (at(e.type),
                [A.UnitTypeEnum.BA, A.UnitTypeEnum.IN].includes(e.type));
                return (0,
                b.jsxs)("div", {
                    children: [(0,
                    b.jsxs)(r.A.Label, {
                        className: "home-label mt-2 mb-0",
                        children: [(0,
                        b.jsx)("i", {
                            className: "fab fa-hive"
                        }), " BattleTech: Override - Card Builder"]
                    }), (0,
                    b.jsx)("hr", {
                        className: "mt-0 mb-2 home-hr",
                        style: {
                            borderColor: "#fff"
                        }
                    }), (0,
                    b.jsxs)(r.A, {
                        children: [(0,
                        b.jsx)(r.A.Row, {
                            className: "mb-0",
                            children: (0,
                            b.jsxs)("div", {
                                className: "mb-2 ml-0",
                                children: [e.isImportSupported(A.ImportTypeEnum.MML) ? (0,
                                b.jsx)(i.A, {
                                    onClick: e => {
                                        e.show = !0,
                                        this.handleShowImport(e)
                                    }
                                    ,
                                    className: "ml-1 mb-1",
                                    disabled: this.getDestinyInverse(),
                                    style: {
                                        width: "100px"
                                    },
                                    children: "Import"
                                }) : null, (0,
                                b.jsx)(i.A, {
                                    onClick: this.handleCardDownload,
                                    className: "ml-1 mb-1",
                                    style: {
                                        width: "100px"
                                    },
                                    children: "Download"
                                })]
                            })
                        }), (0,
                        b.jsxs)(r.A.Row, {
                            children: [(0,
                            b.jsx)(s.A, {
                                lg: 12,
                                xl: 6,
                                children: (0,
                                b.jsx)(l.A, {
                                    defaultActiveKey: "unit",
                                    id: "formTabs",
                                    className: "h6",
                                    transition: !1,
                                    children: (0,
                                    b.jsx)(o.A, {
                                        eventKey: "unit",
                                        title: "Unit Data",
                                        children: (0,
                                        b.jsx)(te, {
                                            unit: e,
                                            onChange: this.handleChangeUnit,
                                            onReset: this.handleResetUnit,
                                            onAddItem: this.handleAddUnitItem,
                                            onRemoveItem: this.handleRemoveUnitItem,
                                            onChangeItem: this.handleChangeUnitItem,
                                            onSortItems: this.handleSortUnitItems,
                                            onGroupWeapons: this.handleGroupUnitWeapons,
                                            onClearItems: this.handleClearUnitItems,
                                            errors: a
                                        })
                                    })
                                })
                            }), (0,
                            b.jsx)(s.A, {
                                lg: 12,
                                xl: 6,
                                children: m ? (0,
                                b.jsx)(za, {
                                    data: n,
                                    width: Ya,
                                    height: Za,
                                    stageRef: this.stageRef,
                                    onDownload: this.handleCardDownload,
                                    isFontsLoaded: this.state.isFontsLoaded
                                }) : (0,
                                b.jsx)(Ra, {
                                    data: n,
                                    width: Ya,
                                    height: Za,
                                    stageRef: this.stageRef,
                                    onDownload: this.handleCardDownload,
                                    isFontsLoaded: this.state.isFontsLoaded
                                })
                            })]
                        })]
                    }), this.state.showImport ? (0,
                    b.jsx)(Ka, {
                        unit: e,
                        onHide: this.handleShowImport,
                        onImport: this.handleImport
                    }) : null]
                })
            }
            componentDidMount() {
                this.fontDetection()
            }
            handleChangeUnit(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = e.currentTarget
                  , t = "checkbox" === a.type ? a.checked : a.value
                  , n = a.id
                  , s = n.split(".")
                  , r = et(this.state.unit, n, t, s);
                this.setState(e => ({
                    unit: r
                }))
            }
            handleAddUnitItem(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = e.currentTarget.dataset.item
                  , t = this.state.unit.clone();
                "weapons" === a ? t.addWeapon() : "equipment" === a && t.addEquipment(),
                this.setState(e => ({
                    unit: t
                }))
            }
            handleRemoveUnitItem(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = e.currentTarget.dataset.item
                  , t = e.currentTarget.value
                  , n = this.state.unit.clone();
                "weapons" === a ? n.removeWeapon(t) : "equipment" === a && n.removeEquipment(t),
                this.setState(e => ({
                    unit: n
                }))
            }
            handleChangeUnitItem(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = e.currentTarget.dataset.item
                  , t = e.currentTarget.dataset.index
                  , n = e.currentTarget.dataset.property
                  , s = e.currentTarget.value
                  , r = this.state.unit.clone();
                "weapons" === a ? r.changeWeapon(t, n, s) : "equipment" === a && r.changeEquipment(t, n, s),
                this.setState(e => ({
                    unit: r
                }))
            }
            handleSortUnitItems(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = this.state.unit.clone();
                a.sortWeapons(),
                a.sortEquipment(),
                this.setState(e => ({
                    unit: a
                }))
            }
            handleClearUnitItems(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = this.state.unit.clone();
                a.weapons = [],
                a.equipment = [],
                this.setState(e => ({
                    unit: a
                }))
            }
            handleResetUnit(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = new L;
                this.setState(e => ({
                    unit: a,
                    unitErrors: {}
                }))
            }
            handleChangePilot(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = e.currentTarget
                  , t = "checkbox" === a.type ? a.checked : a.value
                  , n = a.id
                  , s = Object.assign(new le, this.state.pilot);
                s[n] = t,
                this.setState(e => ({
                    pilot: s
                }))
            }
            handleResetPilot(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = new le;
                this.setState(e => ({
                    pilot: a,
                    pilotErrors: {}
                }))
            }
            handleCardDownload() {
                const e = this.state.unit
                  , a = this.state.pilot
                  , t = this.stageRef.current;
                if (!t)
                    return;
                const n = t.clone();
                n.size({
                    width: Ya,
                    height: Za
                }),
                n.scale({
                    x: 1,
                    y: 1
                });
                let s = "";
                s += e.chassis ? "_" + e.chassis.replace(/[^a-z0-9]/gi, "").toLowerCase() : "",
                s += e.variant ? "_" + e.variant.replace(/[^a-z0-9]/gi, "").toLowerCase() : "",
                s += a.pilotName ? "_" + a.pilotName.replace(/[^a-z0-9]/gi, "").toLowerCase() : "",
                s = "btd" + s + ".png";
                const r = document.createElement("a");
                r.download = s,
                r.href = n.toDataURL(),
                document.body.appendChild(r),
                r.click(),
                document.body.removeChild(r),
                n.destroy(),
                m.A.analytics().logEvent("card_download", {
                    unit_type: e.typeName,
                    chassis: e.chassis,
                    variant: e.variant
                })
            }
            handleShowImport(e) {
                this.setState({
                    showImport: e.show
                })
            }
            handleImport(e) {
                if (e) {
                    var a = e.clone();
                    a.autoGroupWeaponsV5(),
                    a.sortEquipment(),
                    this.setState(e => ({
                        unit: a,
                        unitErrors: {}
                    })),
                    m.A.analytics().logEvent("card_import", {
                        unit_type: e.typeName,
                        chassis: e.chassis,
                        variant: e.variant
                    })
                }
            }
            handleGroupUnitWeapons(e) {
                if (!e || !e.currentTarget)
                    return;
                const a = this.state.unit.clone();
                a.autoGroupWeaponsV5(),
                this.setState(e => ({
                    unit: a
                }))
            }
        }
        const et = (e, a, t, n) => {
            let s = null;
            if ("type" === a)
                switch (t) {
                case A.UnitTypeEnum.BM:
                    s = new L(e);
                    break;
                case A.UnitTypeEnum.AF:
                    s = new K(e);
                    break;
                case A.UnitTypeEnum.CV:
                    s = new X(e);
                    break;
                case A.UnitTypeEnum.BA:
                    s = new D(e);
                    break;
                case A.UnitTypeEnum.IN:
                    s = new J(e);
                    break;
                default:
                    s = new L(e)
                }
            else if (s = e.clone(),
            n.length > 1) {
                const a = Object.assign({}, e[n[0]]);
                a[n[1]] = t,
                s[n[0]] = a
            } else
                s[a] = t;
            return s
        }
          , at = e => {
            switch (e) {
            case A.UnitTypeEnum.CV:
                return "Crew Data";
            case A.UnitTypeEnum.BA:
            case A.UnitTypeEnum.IN:
                return "Officer Data";
            default:
                return "Pilot Data"
            }
        }
          , tt = (e, a) => ({
            unitBlank: e.isBlank,
            unitName: e.cardName,
            unitType: e.type,
            unitTypeName: e.typeName,
            motiveType: e.motiveType,
            squadSize: e.squadSize,
            squadCount: e.squadCount,
            mass: e.tonnage,
            move: e.destinyMove,
            tmm: e.destinyTMM,
            sinks: e.destinySinks,
            hasHeat: "sinks"in e && e.motiveType !== K.MotiveTypeEnum.CF,
            damageThreshold: e.damageThreshold,
            weapons: e.destinyWeapons,
            equipment: e.destinyEquipment,
            hasTurret: e.hasTurret || !1,
            hasAntiMech: e.hasAntiMech || !1,
            hasMechanized: e.hasMechanized || !1,
            pilotBlank: a.pilotBlank,
            pilotName: a.pilotName,
            skillsCost: a.skillsCost,
            skillsRank: a.skillsRank,
            edge: a.edge,
            gunnery: a.gunneryTW,
            piloting: a.pilotingTW,
            tactics: a.tacticsTW,
            leadership: a.leadershipTW,
            guts: a.gutsTW,
            condition: Math.max(a.strength, 1),
            pips: nt(e),
            sliceStructurePips: e.isEquipedWith("reinforced"),
            sliceArmorPips: e.isEquipedWith("hardened"),
            sliceTwice: e.isEquipedWith("ferolam"),
            greenPips: e.isEquipedWith("lasrefl"),
            bluePips: e.isEquipedWith("reactive"),
            brownPips: e.isEquipedWith("ballreinf"),
            purplePips: e.isEquipedWith("stealth"),
            baorangePips: e.isEquipedWith("bafireresist"),
            barainbowPips: e.isEquipedWith("bamimetic"),
            babluePips: e.isEquipedWith("bareactive"),
            bagreenPips: e.isEquipedWith("bareflective"),
            bapurplePips: e.isEquipedWith("bastealth")
        })
          , nt = e => {
            var a = {};
            return e.destinyLocations.forEach(t => {
                a[t] = {
                    armor: e.destinyArmorValue(t),
                    structure: e.destinyStructureValue(t)
                }
            }
            ),
            a
        }
          , st = $a
    }
}]);