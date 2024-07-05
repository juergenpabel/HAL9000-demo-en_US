#!/usr/bin/env python3

from dbus_fast.aio import MessageBus
from dbus_fast.auth import AuthExternal, UID_NOT_SPECIFIED
from dbus_fast.constants import BusType
import asyncio

async def main():
	bus = await MessageBus(None, BusType.SYSTEM, AuthExternal(UID_NOT_SPECIFIED)).connect()
	introspection = await bus.introspect('org.freedesktop.login1', '/org/freedesktop/login1')
	obj = bus.get_proxy_object('org.freedesktop.login1', '/org/freedesktop/login1', introspection)
	manager = obj.get_interface('org.freedesktop.login1.Manager')
	await manager.call_reboot(True)

asyncio.run(main())

