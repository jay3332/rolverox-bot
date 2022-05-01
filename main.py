if __name__ == '__main__':
    import uvloop

    uvloop.install()
    del uvloop

    from core.bot import Rolverox

    Rolverox().run()
