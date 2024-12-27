from typing import ClassVar

from pydantic import BaseModel, ConfigDict

from api.widgets.settings import MySwitch


class Main(BaseModel):
    class DisableSplashscreens(BaseModel):
        model_config = ConfigDict(arbitrary_types_allowed=True)
        default_value: bool = False
        type: ClassVar = MySwitch

    class RetroEffects(BaseModel):
        model_config = ConfigDict(arbitrary_types_allowed=True)
        default_value: bool = False
        type: ClassVar = MySwitch

    disable_splashscreens: DisableSplashscreens = DisableSplashscreens()
    retro_effects: RetroEffects = RetroEffects()
