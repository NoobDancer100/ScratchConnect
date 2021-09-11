from scratchclient import ScratchSession
from windows.login import Login
from windows.home import Home
if __name__ == '__main__':
    info = Login()
    session: ScratchSession
    @info.onDone
    def done(username,password):
        global session
        session = ScratchSession(username,password)
    info.readInfo()
    if session:
        home = Home(session)
        home.launch()