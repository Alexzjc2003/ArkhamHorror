from __future__ import annotations

from event.event_type import EventType
from event.select_target import SelectTargetEvent, TResult

from .event_listener import EventListener, Handle


class TargetSelector(EventListener):
    @Handle(EventType.SelectTarget)
    def select(self, event: SelectTargetEvent[TResult]):
        amount = event.amount
        options = event.options
        if len(options) == 0 or amount == 0:
            event.setCancelled()
            return

        if amount == 1:
            print(f"{event.prompt}: ")
            opts: list[TResult] = []
            for opt, info in event.options.items():
                print(f"{len(opts)}")
                if info is not None:
                    print(f"  {info}")
                opts.append(opt)

            idx = int(input("Type the index: "))
            event.target = opts[idx]
            pass
        if amount == -1:
            pass
        else:
            pass
