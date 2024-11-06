from collections.abc import Iterator, Sequence

from pydantic import BaseModel

from cmk.server_side_calls.v1 import (
    ActiveCheckCommand,
    ActiveCheckConfig,
)


class RdpParams(BaseModel):
    service_description: str | None = None
    hostname: str | None = None
    port: int | None = None
    warn: int | None = None
    crit: int | None = None



def generate_rdp_commands(params, _host_config):
    args = (
        "-H",
        params.hostname or _host_config.primary_ip_config.address,
        "-p",
        f"{params.port or 3389}",
        "-w",
        f"{params.warn or 1}",
        "-c",
        f"{params.crit or 5}",
    )

    yield ActiveCheckCommand(service_description=params.service_description, command_arguments=args)


active_check_rdp = ActiveCheckConfig(
    name="rdp_x224",
    parameter_parser=RdpParams.model_validate,
    commands_function=generate_rdp_commands,
)