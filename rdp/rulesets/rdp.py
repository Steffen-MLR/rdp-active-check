#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-


from cmk.rulesets.v1 import Help, Title
from cmk.rulesets.v1.form_specs import (
    DictElement,
    Dictionary,
    DefaultValue,
    Integer,
    String,
    TimeMagnitude,
    TimeSpan,
)

from cmk.rulesets.v1.rule_specs import ActiveCheck, Topic

def _parameter_form() -> Dictionary:
    return Dictionary(
        title=Title("Check RDP Service"),
        help_text=Help("This check alerts when RDP is not accessible delayed"
            "This check uses the active check <tt>active_check_rdp</tt>. "),
        elements={
            "service_description": DictElement(
                required=True,
                parameter_form=String(
                    title=Title("Service Name"),
                    prefill=DefaultValue("RDP"),
                ),
            ),
            "hostname": DictElement(
                parameter_form=String(
                    title=Title("DNS Hostname or IP address"),
                    help_text=Help('You can specify a hostname or IP address different from IP address of the host as configured in your host properties.'),
                    prefill=DefaultValue("$HOSTADDRESS$"),
                ),
            ),
            "port": DictElement(
                parameter_form=Integer(
                    title=Title("RDP Port"),
                    prefill=DefaultValue(3389),
                ),
            ),
            "warn": DictElement(
                parameter_form=TimeSpan(
                    title=Title("Seconds until Warn State"),
                    displayed_magnitudes=[TimeMagnitude.SECOND],
                    #migrate=float,  # type: ignore[arg-type]  # wrong type, but desired behaviour.
                    prefill=DefaultValue(60.0),
                ),
            ),
            "crit": DictElement(
                parameter_form=TimeSpan(
                    title=Title("Seconds until Crit State"),
                    displayed_magnitudes=[TimeMagnitude.SECOND],
                    #migrate=float,  # type: ignore[arg-type]  # wrong type, but desired behaviour.
                    prefill=DefaultValue(60.0),
                ),
            ),
        }
    )

rule_spec_active_check_rdp = ActiveCheck(
    title=Title("Check RDP Service"),
    help_text=Help("This check alerts when RDP is not accessible delayed"
               "This check uses the active check <tt>active_check_rdp</tt>. "),
    name="rdp_x224",
    topic=Topic.WINDOWS,
    parameter_form=_parameter_form,
)