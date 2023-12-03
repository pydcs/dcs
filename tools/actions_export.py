actions = {
    "MessageToAll": {
        "name": "a_out_text_delay",
        "fields": [
            {
                "id": "text",
                "type": "medit",
                "default": "",
            },
            {
                "id": "seconds",
                "type": "spin",
                "default": 10,
            },
            {
                "id": "clearview",
                "type": "checkbox",
                "default": False,
            }
        ]
    },

    "MessageToCoalition": {
        "name": "a_out_text_delay_s",
        "fields": [
            {
                "id": "coalitionlist",
                "type": "combo",

                "default": "",
            },
            {
                "id": "text",
                "type": "medit",
                "default": "",

            },
            {
                "id": "seconds",
                "type": "spin",
                "default": 10,

            },
            {
                "id": "clearview",
                "type": "checkbox",
                "default": False,
            },
        ]
    },

    "MessageToGroup": {
        "name": "a_out_text_delay_g",
        "fields": [
            {
                "id": "group",
                "type": "combo",

                "default": "",
            },
            {
                "id": "text",
                "type": "medit",
                "default": "",

            },
            {
                "id": "seconds",
                "type": "spin",
                "default": 10,

            },
            {
                "id": "clearview",
                "type": "checkbox",
                "default": False,
            },
        ]
    },

    "MessageToCountry": {
        "name": "a_out_text_delay_c",
        "fields": [
            {
                "id": "countrylist",
                "type": "combo",

                "default": "",
            },
            {
                "id": "text",
                "type": "medit",
                "default": "",

            },
            {
                "id": "seconds",
                "type": "spin",
                "default": 10,

            },
            {
                "id": "clearview",
                "type": "checkbox",
                "default": False,
            },
        ]
    },

    "SetFlag": {
        "name": "a_set_flag",
        "fields": [
            {"id": "flag", "default": 1},
        ]
    },

    "ClearFlag": {
        "name": "a_clear_flag",
        "fields": [
            {"id": "flag", "default": 1},
        ]
    },

    "SetFlagValue": {
        "name": "a_set_flag_value",
        "fields": [
            {"id": "flag", "default": 1},
            {"id": "value", "default": 1}
        ]
    },

    "SetFlagRandom": {
        "name": "a_set_flag_random",
        "fields": [
            {"id": "flag", "default": 1},
            {
                "id": "min_value",
                "default": 0,
            },
            {
                "id": "max_value",
                "default": 100,
            },
        ]
    },

    "IncreaseFlag": {
        "name": "a_inc_flag",
        "fields": [
            {"id": "flag", "default": 1},
            {
                "id": "value",
                "default": 10,

            },
        ]
    },

    "DecreaseFlag": {
        "name": "a_dec_flag",
        "fields": [
            {"id": "flag", "default": 1},
            {
                "id": "value",
                "default": 10,
            },
        ]
    },

    "SoundToAll": {
        "name": "a_out_sound",
        "fields": [
            {
                "id": "file",
                "type": "file_edit",
                "default": "",
            },
        ]
    },
    "StopLastSound": {
        "name": "a_out_sound_stop",
        "fields": []
    },
    "SoundToCoalition": {
        "name": "a_out_sound_s",
        "fields": [
            {
                "id": "coalitionlist",
                "type": "combo",

                "default": "",
            },
            {
                "id": "file",
                "type": "file_edit",
                "default": "",
            },
        ]
    },

    "SoundToGroup": {
        "name": "a_out_sound_g",
        "fields": [
            {
                "id": "group",
                "type": "combo",

                "default": "",
            },
            {
                "id": "file",
                "type": "file_edit",
                "default": "",
            },
        ]
    },

    "SoundToUnit": {
        "name": "a_out_sound_u",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
            {
                "id": "file",
                "type": "file_edit",
                "default": "",
            },
        ]
    },

    "SoundToCountry": {
        "name": "a_out_sound_c",
        "fields": [
            {
                "id": "countrylist",
                "type": "combo",

                "default": "",
            },
            {
                "id": "file",
                "type": "file_edit",
                "default": "",
            },
        ]
    },

    "ActivateGroup": {
        "name": "a_activate_group",
        "fields": [
            {
                "id": "group",
                "type": "combo",
                "default": "",

            },
        ]
    },

    "FallInTemplate": {
        "name": "a_fall_in_template",
        "fields": [
            {
                "id": "group",
                "type": "combo",
                "default": "",
            },
            {
                "id": "template",
                "type": "combo",
                "default": "",
            },
        ]
    },

    "DeactivateGroup": {
        "name": "a_deactivate_group",
        "fields": [
            {
                "id": "group",
                "type": "combo",
                "default": "",
            },
        ]
    },

    "EndMission": {
        "name": "a_end_mission",
        "fields": [
            {
                "id": "winner",
                "type": "combo",
                "default": "",
            },
            {
                "id": "text",
                "type": "medit",
                "default": "",
            },
        ]
    },

    "SetFailure": {
        "name": "a_set_failure",
        "fields": [
            {
                "id": "failure",
                "default": "",
            },
            {
                "id": "probability",
                "type": "spin",
                "default": 100,

            },
            {
                "id": "random_pause",
                "type": "spin",
                "default": 0,

            }
        ]
    },

    "SetInternalCargo": {
        "name": "a_set_internal_cargo",
        "fields": [
            {
                "id": "cargo_mass",
                "type": "spin",
                "default": 100,
            },
        ]
    },

    "Explosion": {
        "name": "a_explosion",
        "fields": [
            {
                "id": "zone",
                "type": "combo",
                "default": "",
            },
            {
                "id": "altitude",
                "type": "spin",
                "default": 1,
            },
            {
                "id": "volume",
                "type": "spin",
                "default": 1000,
            },
        ]
    },

    "ExplodeUnit": {
        "name": "a_explosion_unit",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
            {
                "id": "volume",
                "type": "spin",
                "default": 1000,
            },
        ]
    },
    "ExplodeWPMarker": {
        "name": "a_explosion_marker",
        "fields": [
            {
                "id": "zone",
                "type": "combo",
                "default": "",
            },
            {
                "id": "altitude",
                "type": "spin",
                "default": 1,
            },
            {
                "id": "color",
                "type": "combo",
                "default": "0",
            },
        ]
    },
    "ExplodeWPMarkerOnUnit": {
        "name": "a_explosion_marker_unit",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
            {
                "id": "color",
                "type": "combo",
                "default": "0",
            },
        ]
    },
    "IlluminatingBomb": {
        "name": "a_illumination_bomb",
        "fields": [
            {
                "id": "zone",
                "type": "combo",

                "default": "",

            },
            {
                "id": "altitude",
                "type": "spin",
                "default": 1,

            },
        ]
    },
    "SignalFlare": {
        "name": "a_signal_flare",
        "fields": [
            {
                "id": "zone",
                "type": "combo",
                "default": "",
            },
            {
                "id": "altitude",
                "type": "spin",
                "default": 1,
            },
            {
                "id": "color",
                "type": "combo",
                "default": "0",
            },
            {
                "id": "bearing",
                "type": "spinbearing",
                "default": "0",
            },
        ]
    },
    "SignalFlareOnUnit": {
        "name": "a_signal_flare_unit",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
            {
                "id": "color",
                "type": "combo",
                "default": "0",
            },
            {
                "id": "bearing",
                "type": "spinbearing",
                "default": "0",
            },
        ]
    },
    "PlayArgument": {
        "name": "a_play_argument",
        "fields": [
            {
                "id": "object",
                "type": "combo",
            },
            {
                "id": "argument",
                "type": "spin",
                "default": 0
            },
            {
                "id": "start",
                "default": 0,

            },
            {
                "id": "stop",
                "default": 1,

            },
            {
                "id": "speed",
                "default": 1,
            },
        ]
    },
    "LoadMission": {
        "name": "a_load_mission",
        "fields": [
            {
                "id": "file",
                "type": "file_miz",
                "default": "",
            },
        ]
    },
    "CockpitHighlightElement": {
        "name": "a_cockpit_highlight",
        "fields": [
            {
                "id": "highlight_id",
                "default": 0,
            },
            {
                "id": "element_name",
                "default": "",
            },
            {
                "id": "size_of_box",
                "default": 0,
            },
        ]
    },
    "CockpitHighlightPosition": {
        "name": "a_cockpit_highlight_position",
        "fields": [
            {
                "id": "highlight_id",
                "default": 0,
            },
            {
                "id": "in_cockpit_position_x",
                "default": 1,
            },
            {
                "id": "in_cockpit_position_y",
                "default": 0,
            },
            {
                "id": "in_cockpit_position_z",
                "default": 0,
            },
            {
                "id": "size_of_box_x",
                "default": 0.1,
            },
            {
                "id": "size_of_box_y",
                "default": 0.1,
            },
            {
                "id": "size_of_box_z",
                "default": 0.1,
            },
        ]
    },
    "CockpitHighlightIndication": {
        "name": "a_cockpit_highlight_indication",
        "fields": [
            {
                "id": "highlight_id",
                "default": 0,
            },
            {
                "id": "indicator_id",
                "default": 0,
            },
            {
                "id": "element_name",
                "default": "",
            },
            {
                "id": "size_of_box",
                "default": 0,
            },
        ]
    },
    "CockpitRemoveHighlight": {
        "name": "a_cockpit_remove_highlight",
        "fields": [
            {
                "id": "highlight_id",

                "default": 0,

            },
        ]
    },
    "StartWaitUserResponse": {
        "name": "c_start_wait_for_user",
        "fields": [
            {"id": "flag", "default": 1},
            {"id": "flag_black", "default": 999}
        ]
    },
    "StopWaitUserResponse": {
        "name": "c_stop_wait_for_user",
        "fields": []
    },
    "SetCommand": {
        "name": "a_set_command",
        "fields": [
            {
                "id": "command",
                "default": 0,
            },
        ]
    },
    "SetCommandWithValue": {
        "name": "a_set_command_with_value",
        "fields": [
            {
                "id": "command",
                "default": 0,
            },
            {
                "id": "value",
                "default": 0,
            },
        ]
    },
    "StartListenCommand": {
        "name": "a_start_listen_command",
        "fields": [
            {
                "id": "command",
                "default": 0,
            },
            {"id": "flag", "default": 1},
            {
                "id": "hit_count",
                "default": 0,
            },
            {
                "id": "min_value",
                "default": -1000000,
            },
            {
                "id": "max_value",
                "default": 1000000,
            },
            {
                "id": "cockpit_device",
                "default": 0,
            },
        ]
    },
    "StartListenCockpitEvent": {
        "name": "a_start_listen_event",
        "fields":
            [
                {
                    "id": "event",
                    "default": "",
                },
                {"id": "flag", "default": 1},
            ]
    },
    "CockpitPerformClickableAction": {
        "name": "a_cockpit_perform_clickable_action",
        "fields": [
            {
                "id": "cockpit_device",
                "default": 0,
            },
            {
                "id": "command",
                "default": 3001,
            },
            {
                "id": "value",
                "default": 0,
            },
        ]
    },
    "CockpitParamSaveAs": {
        "name": "a_cockpit_param_save_as",
        "fields": [
            {
                "id": "source",
                "default": "",
            },
            {
                "id": "destination",
                "default": "",
            },
        ]
    },
    "AddRadioItem": {
        "name": "a_add_radio_item",
        "fields": [
            {
                "id": "radiotext",
                "type": "text",
            },
            {"id": "flag", "default": 1},
            {"id": "value", "default": 1}
        ]
    },
    "RemoveRadioItem": {
        "name": "a_remove_radio_item",
        "fields": [
            {
                "id": "radiotext",
                "type": "text",
            }
        ]
    },
    "AddRadioItemForCoalition": {
        "name": "a_add_radio_item_for_coalition",
        "fields": [
            {
                "id": "coalitionlist",
                "type": "combo",
                "default": "all",
            },
            {
                "id": "radiotext",
                "type": "text",
            },
            {"id": "flag", "default": 1},
            {"id": "value", "default": 1}
        ]
    },
    "RemoveRadioItemForCoalition": {
        "name": "a_remove_radio_item_for_coalition",
        "fields": [
            {
                "id": "coalitionlist",
                "type": "combo",
                "default": "all",
            },
            {
                "id": "radiotext",
                "type": "text",
            }
        ]
    },
    "AddRadioItemForGroup": {
        "name": "a_add_radio_item_for_group",
        "fields": [
            {
                "id": "group",
                "type": "combo",
                "default": "",
            },
            {
                "id": "radiotext",
                "type": "text",
            },
            {"id": "flag", "default": 1},
            {"id": "value", "default": 1}
        ]
    },
    "RemoveRadioItemForGroup": {
        "name": "a_remove_radio_item_for_group",
        "fields": [
            {
                "id": "group",
                "type": "combo",
                "default": "",

            },
            {
                "id": "radiotext",
                "type": "text",
            }
        ]
    },
    "GroupStop": {
        "name": "a_group_stop",
        "fields": [
            {
                "id": "group",
                "type": "combo",
                "default": "",
            },
        ]
    },
    "GroupResume": {
        "name": "a_group_resume",
        "fields": [
            {
                "id": "group",
                "type": "combo",
                "default": "",
            },
        ]
    },
    "GroupAIOn": {
        "name": "a_group_on",
        "fields": [
            {
                "id": "group",
                "type": "combo",
                "default": "",
            },
        ]
    },
    "GroupAIOff": {
        "name": "a_group_off",
        "fields": [
            {
                "id": "group",
                "type": "combo",
                "default": "",
            },
        ]
    },
    "UnitAIOn": {
        "name": "a_unit_on",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
        ]
    },
    "UnitAIOff": {
        "name": "a_unit_off",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
        ]
    },
    "UnitEmissionOn": {
        "name": "a_unit_emission_on",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
        ]
    },
    "UnitEmissionOff": {
        "name": "a_unit_emission_off",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
        ]
    },
    # "SetAITask": {
    #     "name": "a_set_ai_task",
    #     "fields": [
    #         {
    #             "id": "set_ai_task",
    #             "type": "combo",
    #             "default": {"", ""},
    #         }
    #     ]
    # },
    # "PushAITask": {
    #     "name": "a_ai_task",
    #     "fields": [
    #         {
    #             "id": "ai_task",
    #             "type": "combo",
    #             "default": {"", ""},
    #         }
    #     ]
    # },
    "PreventControlsSynchronization": {
        "name": "a_prevent_controls_synchronization",
        "fields": [{"id": "value", "default": False}]
    },
    "RadioTransmission": {
        "name": "a_radio_transmission",
        "fields": [
            {
                "id": "file",
                "type": "file_edit",
                "default": "",
            },
            {
                "id": "zone",
                "type": "combo",
                "default": "",
            },
            {"id": "modulation", "default": False},
            {
                "id": "loop",
                "default": False,
            },
            {
                "id": "frequency",
                "default": 124000,
            },
            {
                "id": "power",
                "default": 100,
            },
            {
                "id": "name",
                "type": "text",
            }
        ]
    },
    "StopRadioTransmission": {
        "name": "a_stop_radio_transmission",
        "fields": [
            {
                "id": "name",
                "type": "text",
            }
        ]
    },
    "ShowHelperGate": {
        "name": "a_show_helper_gate",
        "fields": [
            {
                "id": "x",

                "default": 0,
            },
            {
                "id": "z",

                "default": 0,
            },
            {
                "id": "y",

                "default": 0,
            },
            {
                "id": "course",

                "default": 0,
            },
        ]
    },
    "ShowHelperGatesForUnit": {
        "name": "a_show_route_gates_for_unit",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
            {"id": "flag", "default": 1},
        ]
    },
    "SetActiveHelperGateToPoint": {
        "name": "a_route_gates_set_current_point",
        "fields": [
            {
                "id": "unit",
                "type": "combo",
                "default": "",
            },
            {
                "id": "number",
                "default": 1,
            },
        ]
    },
    "DoScript": {
        "name": "a_do_script",
        "fields": [
            {
                "id": "text",
                "type": "medit",
                "default": "",
            }
        ]
    },
    "DoScriptFile": {
        "name": "a_do_script_file",
        "fields": [
            {
                "id": "file",
                "type": "file_script",
                "default": "",
            }
        ]
    },
    "BeginPlayingActor": {
        "name": "a_cockpit_push_actor",
        "fields":
            [
                {
                    "id": "number",
                    "default": 1,
                }
            ]
    },
    "StopPlayingActor": {
        "name": "a_cockpit_pop_actor",
        "fields": [],
    },
    "StartPlayerSeatLock": {
        "name": "a_cockpit_lock_player_seat",
        "fields": [
            {
                "id": "number",
                "default": 1,
            }
        ]
    },
    "StopPlayerSeatLock": {
        "name": "a_cockpit_unlock_player_seat",
        "fields": [],
    },
}


def genactions(name, d):
    templ = """
class {cl}(Action):
    predicate = "{pred}"

    def __init__(self, {params}):
        super({cl}, self).__init__({cl}.predicate)
        {init}

    @classmethod
    def create_from_dict(cls, d):
        return cls({load})

    def dict(self):
        d = super({cl}, self).dict()
        {out}
        return d
"""
    params = []
    init = []
    load = []
    out = []
    for x in d["fields"]:
        defval = x.get("default", "")
        default = "=" + str(x["default"]) if defval != "" else '=""'
        params.append(x["id"] + default)
        init.append("self.{id} = {id}".format(id=x["id"]))
        init.append("self.params.append(self.{id})".format(id=x["id"]))
        load.append('d["{id}"]'.format(id=x["id"]))
        out.append('d["{id}"] = self.{id}'.format(id=x["id"]))
    print(templ.format(
        cl=name,
        pred=d["name"],
        params=", ".join(params),
        init="\n        ".join(init),
        load=", ".join(load),
        out="\n        ".join(out)))


for x in sorted(actions):
    genactions(x, actions[x])

print("actions_map = {")
for x in sorted(actions):
    print('    "{r}": {cl},'.format(r=actions[x]["name"], cl=x))
print("}")
