from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_helmet(self, update):
        text = update.message.text
        return text.lower() == 'helmet'

    def is_going_to_motogp(self, update):
        text = update.message.text
        return text.lower() == 'motogp'

    def is_going_to_clothes(self, update):
        text = update.message.text
        return text.lower() == 'clothes'

    def is_going_to_shockabsorber(self, update):
        text = update.message.text
        return text.lower() == 'shockabsorber'

    def is_going_to_below2000(self, update):
        text = update.message.text
        return text.lower() == 'below2000'

    def is_going_to_from2000to8000(self, update):
        text = update.message.text
        return text.lower() == 'from2000to8000'

    def is_going_to_above8000(self, update):
        text = update.message.text
        return text.lower() == 'above8000'

    def is_going_to_sol1(self, update):
        text = update.message.text
        return text.lower() == 'sol'

    def is_going_to_sol2(self, update):
        text = update.message.text
        return text.lower() == 'sol'

    def is_going_to_zeus1(self, update):
        text = update.message.text
        return text.lower() == 'zeus'

    def is_going_to_zeus2(self, update):
        text = update.message.text
        return text.lower() == 'zeus'

    def is_going_to_thh1(self, update):
        text = update.message.text
        return text.lower() == 'thh'

    def is_going_to_thh2(self, update):
        text = update.message.text
        return text.lower() == 'thh'

    def is_going_to_agv(self, update):
        text = update.message.text
        return text.lower() == 'agv'

    def on_enter_helmet(self, update):
        update.message.reply_text("ok,how much you could pay?\nbelow2000, from2000to8000, above8000")
        """self.go_back(update)"""

    def on_exit_helmet(self, update):
        print('Leaving helmet')

    def on_enter_motogp(self, update):
        update.message.reply_text("what information do you want to know? personal champion or team champion?")
        self.go_back(update)

    def on_exit_motogp(self, update):
        print('Leaving motogp')


    def on_enter_clothes(self, update):
        update.message.reply_text("ok,here are some famous brands around the world\nDainese, Alpinestar...\nWhich one do you want to understand?")
        self.go_back(update)

    def on_exit_clothes(self, update):
        print('Leaving clothes')

    def on_enter_shockabsorber(self, update):
        update.message.reply_text("ok,here are some famous brands in Taiwan\nGJMS, Windwolf, rpm, msp...\nwhich one do you want to understand?")
        self.go_back(update)

    def on_exit_shockabsorber(self, update):
        print('Leaving shockabsorber')

    def on_enter_below2000(self, update):
        update.message.reply_text("ok, which brand you prefer?\nsol, zeus,or thh ?")
        """self.go_back(update)"""

    def on_exit_below2000(self, update):
        print('Leaving helmet')

    def on_enter_from2000to8000(self, update):
        update.message.reply_text("ok, which brand you prefer?\nsol, zeus,or thh ?")
        """self.go_back(update)"""

    def on_exit_from2000to8000(self, update):
        print('Leaving helmet')

    def on_enter_above8000(self, update):
        update.message.reply_text("ok, which brand you prefer? \nagv ?")
        """self.go_back(update)"""

    def on_exit_above8000(self, update):
        print('Leaving helmet')

    def on_enter_sol1(self, update):
        update.message.reply_text("ok,it's your sol")
        update.message.reply_photo(open("img/sol1.jpeg","rb"))
        self.go_back(update)

    def on_exit_sol1(self, update):
        print('Leaving helmet')

    def on_enter_sol2(self, update):
        update.message.reply_text("ok,it's your sol")
        update.message.reply_photo(open("img/sol2.jpg","rb"))
        self.go_back(update)

    def on_exit_sol2(self, update):
        print('Leaving helmet')

    def on_enter_zeus1(self, update):
        update.message.reply_text("ok,it's your zeus")
        update.message.reply_photo(open("img/zeus1.jpg","rb"))
        self.go_back(update)

    def on_exit_zeus1(self, update):
        print('Leaving helmet')

    def on_enter_zeus2(self, update):
        update.message.reply_text("ok,it's your zeus")
        update.message.reply_photo(open("img/zeus2.jpg","rb"))
        self.go_back(update)

    def on_exit_zeus2(self, update):
        print('Leaving helmet')

    def on_enter_thh1(self, update):
        update.message.reply_text("ok,it's your thh")
        update.message.reply_photo(open("img/thh1.jpg","rb"))
        self.go_back(update)

    def on_exit_thh1(self, update):
        print('Leaving helmet')

    def on_enter_thh2(self, update):
        update.message.reply_text("ok,it's your thh")
        update.message.reply_photo(open("img/thh2.jpg","rb"))
        self.go_back(update)

    def on_exit_thh2(self, update):
        print('Leaving helmet')

    def on_enter_agv(self, update):
        update.message.reply_text("ok,it's your agv pista gp r?")
        update.message.reply_photo(open("img/agv.jpg","rb"))
        self.go_back(update)

    def on_exit_agv(self, update):
        print('Leaving helmet')
