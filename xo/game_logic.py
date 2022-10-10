import typing

if typing.TYPE_CHECKING:
    from communication.protocl import CommunicationProtocol


class GameLogic:
    def start_new_p2p_gane(self, connection: CommunicationProtocol):
        ...
