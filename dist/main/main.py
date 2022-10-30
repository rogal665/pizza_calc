import pandas as pd
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class ChangeData(Popup):

    def save(self):
        app = App.get_running_app()
        comp_id = app.Comp_id.split()
        components = pd.read_csv('skladniki.csv', encoding='utf-8', header=0)
        try:
            float(self.ids.change.text)
            components.iloc[int(comp_id[0]), int(comp_id[1])] = self.ids.change.text
        except:
            pass
        components.to_csv('skladniki.csv', encoding='utf-8',index=None)
        App.get_running_app().root.current = 'comp_change'

class ChangeDataDelete(Popup):
    def delete(self):
        app = App.get_running_app()
        comp_id = app.Comp_id.split()
        components = pd.read_csv('skladniki.csv', encoding='utf-8', header=0)
        components.drop(int(comp_id[0]), axis=0, inplace=True)
        components.to_csv('skladniki.csv', encoding='utf-8', index=None)
        App.get_running_app().root.current = 'comp_change'

    def save(self):
        app = App.get_running_app()
        comp_id = app.Comp_id.split()
        components = pd.read_csv('skladniki.csv', encoding='utf-8', header=None)
        components.iloc[int(comp_id[0]), int(comp_id[1])] = self.ids.change.text
        components.to_csv('skladniki.csv', encoding='utf-8',index=None)
        App.get_running_app().root.current = 'comp_change'

class ChangePizzaDelete(Popup):
    def delete(self):
        app = App.get_running_app()
        comp_id = app.Comp_id.split()
        pizza = pd.read_csv('pizza.csv', encoding='utf-8', header=0)
        pizza.drop(int(comp_id[0]), axis=0, inplace=True)
        pizza.to_csv('pizza.csv', encoding='utf-8', index=None)
        App.get_running_app().root.current = 'pizza_change'

    def save(self):
        app = App.get_running_app()
        comp_id = app.Comp_id.split()
        pizza = pd.read_csv('pizza.csv', encoding='utf-8', header=0)
        pizza.iloc[int(comp_id[0]), int(comp_id[1])] = self.ids.change.text
        pizza.to_csv('pizza.csv', encoding='utf-8',index=None)
        App.get_running_app().root.current = 'pizza_change'



class NewComp(Popup):
    def save(self):
        app = App.get_running_app()
        components = pd.read_csv('skladniki.csv', encoding='utf-8', header=0)
        try:
            float(self.ids.large.text)
            float(self.ids.med.text)
            float(self.ids.small.text)
            float(self.ids.price.text)
            data = {'Component':[self.ids.name.text],'weight_l':[self.ids.large.text],'weight_m':[self.ids.med.text],'weight_s':[self.ids.small.text],'price_g':[self.ids.price.text]}
            new_component = pd.DataFrame(index=None, data=data)
            components = pd.concat([components, new_component])
            components.to_csv('skladniki.csv', encoding='utf-8', index=None)
        except:
            pass
        App.get_running_app().root.current = 'comp_change'

class NewPizza(Popup):
    def save(self):
        app = App.get_running_app()
        pizza = pd.read_csv('pizza.csv', encoding='utf-8', header=0)

        data = {'pizza':[self.ids.name.text]}
        new_pizza = pd.DataFrame(index=None, data=data)
        pizza = pd.concat([pizza, new_pizza])
        pizza.to_csv('pizza.csv', encoding='utf-8', index=None)

        App.get_running_app().root.current = 'pizza_change'


class Select_Sos(Popup):
    def tomato(self):
        app = App.get_running_app()
        comp_id = app.Comp_id.split()
        pizzas = pd.read_csv('pizza.csv', encoding='utf-8',header=0)
        pizzas.iloc[int(comp_id[0]), int(comp_id[1])] = 'pomidorowy'
        pizzas.to_csv('pizza.csv', encoding='utf-8', index=None)
        App.get_running_app().root.current = 'pizza_change'
    def garlic(self):
        app = App.get_running_app()
        comp_id = app.Comp_id.split()
        pizzas = pd.read_csv('pizza.csv', encoding='utf-8',header=0)
        pizzas.iloc[int(comp_id[0]), int(comp_id[1])] = 'czosnkowy'
        pizzas.to_csv('pizza.csv', encoding='utf-8', index=None)
        App.get_running_app().root.current = 'pizza_change'
    def bbq(self):
        app = App.get_running_app()
        comp_id = app.Comp_id.split()
        pizzas = pd.read_csv('pizza.csv', encoding='utf-8', header=0)
        pizzas.iloc[int(comp_id[0]), int(comp_id[1])] = 'bbq'
        pizzas.to_csv('pizza.csv', encoding='utf-8', index=None)
        App.get_running_app().root.current = 'pizza_change'

class Select_com(Popup):


    def on_open(self):
        self.ids.comp.clear_widgets()
        components = pd.read_csv('skladniki.csv', encoding='utf-8', header=0)
        components.sort_values(by=['Component'], inplace=True)

        def callback(self):
            app = App.get_running_app()
            comp_id = app.Comp_id.split()
            pizzas = pd.read_csv('pizza.csv', encoding='utf-8', header=0)
            pizzas.iloc[int(comp_id[0]), int(comp_id[1])] = str(self.text)
            pizzas.to_csv('pizza.csv', encoding='utf-8', index=None)
            App.get_running_app().root.current = 'pizza_change'


        def callback2(self):
            app = App.get_running_app()
            comp_id = app.Comp_id.split()
            pizzas = pd.read_csv('pizza.csv', encoding='utf-8', header=0)
            pizzas.iloc[int(comp_id[0]), int(comp_id[1])] = ""
            pizzas.to_csv('pizza.csv', encoding='utf-8', index=None)
            App.get_running_app().root.current = 'pizza_change'


        for x in components.index:
            button = Button(text=(str(components.iloc[int(x), 0])), size_hint_y=None, height=50, on_press=callback)

            self.ids.comp.add_widget(button)
        button = Button(text="Nic", size_hint_y=None, height=50, on_press=callback2)

        self.ids.comp.add_widget(button)

class MainWindow(Screen):
    pass


class Components(Screen):
    def on_enter(self):
        self.ids.compo.clear_widgets()
        def callback(self):
            app = App.get_running_app()
            app.Comp_id = self.id
            ChangeData().open()

        def callback_2(self):
            app = App.get_running_app()
            app.Comp_id = self.id
            ChangeDataDelete().open()


        components = pd.read_csv('skladniki.csv', encoding='utf-8', header=0)

        components.sort_values(by=['Component'], inplace=True)

        for x in components.index:

            button = Button(text=(str(components.iloc[int(x),0])), size_hint_y=None, height=50,on_press=callback_2)
            button.id = str(int(x)) + ' ' +'0'
            self.ids.compo.add_widget(button)

            button = Button(text=(str(components.iloc[int(x), 1]) + 'g'), size_hint_y=None, height=50, on_press=callback)
            button.id = str(int(x)) + ' ' +'1'
            self.ids.compo.add_widget(button)

            button = Button(text=(str(components.iloc[int(x), 2]) + 'g'), size_hint_y=None, height=50, on_press=callback)
            button.id = str(int(x)) + ' ' +'2'
            self.ids.compo.add_widget(button)

            button = Button(text=(str(components.iloc[int(x), 3]) + 'g'), size_hint_y=None, height=50, on_press=callback)
            button.id = str(int(x)) + ' ' +'3'
            self.ids.compo.add_widget(button)

            button = Button(text=(str(components.iloc[int(x), 4]) + 'zl'), size_hint_y=None, height=50, on_press=callback)
            button.id = str(int(x)) + ' ' + '4'
            self.ids.compo.add_widget(button)


            label = Label(text="Koszt", size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

            components.iloc[int(x), 5] = round(float(components.iloc[int(x), 1]) * float(components.iloc[int(x), 4]),2)
            label = Label(text=(str(components.iloc[int(x), 5]) + 'zł'), size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

            components.iloc[int(x), 6] = round(float(components.iloc[int(x), 2]) * float(components.iloc[int(x), 4]), 2)
            label = Label(text=(str(components.iloc[int(x), 6]) + 'zł'), size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

            components.iloc[int(x), 7] = round(float(components.iloc[int(x), 3]) * float(components.iloc[int(x), 4]), 2)
            label = Label(text=(str(components.iloc[int(x), 7]) + 'zl'), size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

            label = Label(text="",size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.compo.add_widget(label)

        components.to_csv('skladniki.csv', encoding='utf-8', index=None)

class Comp_Change(Screen):
    def on_enter(self):
        App.get_running_app().root.current = 'comp'

class Pizza_Change(Screen):
    def on_enter(self):
        App.get_running_app().root.current = 'pizza'




class Pizzas(Screen):
    def on_enter(self):
        self.ids.pizza.clear_widgets()

        pizzas = pd.read_csv('pizza.csv', encoding='utf-8')



        def callback(self):
            app = App.get_running_app()
            app.Comp_id = self.id
            Select_Sos().open()
        def callback2(self):
            app = App.get_running_app()
            app.Comp_id = self.id
            Select_com().open()
        def callback3(self):
            app = App.get_running_app()
            app.Comp_id = self.id
            ChangePizzaDelete().open()

        for x in pizzas.index:
            button = Button(text=(str(pizzas.iloc[int(x), 0])), size_hint_y=None, height=50,on_press=callback3)
            button.id = str(int(x)) + ' ' + '0'
            self.ids.pizza.add_widget(button)

            button = Button(text=('sos ' + str(pizzas.iloc[int(x), 1])), size_hint_y=None, height=50,on_press=callback)
            button.id = str(int(x)) + ' ' + '1'
            self.ids.pizza.add_widget(button)

            button = Button(text=(str(pizzas.iloc[int(x), 2])), size_hint_y=None, height=50,on_press=callback2)
            button.id = str(int(x)) + ' ' + '2'
            self.ids.pizza.add_widget(button)

            button = Button(text=(str(pizzas.iloc[int(x), 3])), size_hint_y=None, height=50,on_press=callback2)
            button.id = str(int(x)) + ' ' + '3'
            self.ids.pizza.add_widget(button)

            button = Button(text=(str(pizzas.iloc[int(x), 4])), size_hint_y=None, height=50,on_press=callback2)
            button.id = str(int(x)) + ' ' + '4'
            self.ids.pizza.add_widget(button)

            button = Button(text=(str(pizzas.iloc[int(x), 5])), size_hint_y=None, height=50,on_press=callback2)
            button.id = str(int(x)) + ' ' + '5'
            self.ids.pizza.add_widget(button)

            button = Button(text=(str(pizzas.iloc[int(x), 6])), size_hint_y=None, height=50,on_press=callback2)
            button.id = str(int(x)) + ' ' + '6'
            self.ids.pizza.add_widget(button)

            button = Button(text=(str(pizzas.iloc[int(x), 7])), size_hint_y=None, height=50,on_press=callback2)
            button.id = str(int(x)) + ' ' + '7'
            self.ids.pizza.add_widget(button)

            button = Button(text=(str(pizzas.iloc[int(x), 8])), size_hint_y=None, height=50,on_press=callback2)
            button.id = str(int(x)) + ' ' + '8'
            self.ids.pizza.add_widget(button)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.pizza.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.pizza.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.pizza.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.pizza.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.pizza.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.pizza.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.pizza.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.pizza.add_widget(label)

            label = Label(text="", size_hint_y=None, height=50)
            self.ids.pizza.add_widget(label)

class Calc(Screen):
    def on_enter(self):


        components = pd.read_csv('skladniki.csv', encoding='utf-8', )
        pizzas = pd.read_csv('pizza.csv', encoding='utf-8', )
        pizzas_price = pizzas[['pizza']].copy()
        pizzas_price['price_l'] = 0
        pizzas_price['price_m'] = 0
        pizzas_price['price_s'] = 0
        i = 0


        for pizza in pizzas.index:
            row = pizzas.iloc[pizza, :].tolist()

            row.pop(0)
            for comp in row:
                if comp in pizzas.loc[i, ['skl1', 'skl2', 'skl3', 'skl4', 'skl5', 'skl6', 'skl7', 'skl8']].values:

                    for index, row2 in components.iterrows():
                        if row2['Component'] == comp:
                            pizzas_price.loc[i, ['price_l']] = pizzas_price.loc[i, ['price_l']] + row2['price_l']
                            pizzas_price.loc[i, ['price_m']] = pizzas_price.loc[i, ['price_m']] + row2['price_m']
                            pizzas_price.loc[i, ['price_s']] = pizzas_price.loc[i, ['price_s']] + row2['price_s']
            i = i + 1

        pizzas_price.price_l = pizzas_price.price_l + \
                               components[components['Component'] == 'ser']['price_l'].values[0] + \
                               components[components['Component'] == 'ciasto']['price_l'].values[0] + \
                               components[components['Component'] == 'sos']['price_l'].values[0]
        pizzas_price.price_m = pizzas_price.price_m + \
                               components[components['Component'] == 'ser']['price_m'].values[0] + \
                               components[components['Component'] == 'ciasto']['price_m'].values[0] + \
                               components[components['Component'] == 'sos']['price_m'].values[0]
        pizzas_price.price_s = pizzas_price.price_s + \
                               components[components['Component'] == 'ser']['price_s'].values[0] + \
                               components[components['Component'] == 'ciasto']['price_s'].values[0] + \
                               components[components['Component'] == 'sos']['price_s'].values[0]


        pizzas_price.to_csv("pizza_cena.csv", index=None)
        self.ids.calc.clear_widgets()

        #print(components[components['Component']=='ser']['price_l'].values[0])
        self.ids.ser.text='Ser    Duża: ' + str(components[components['Component']=='ser']['price_l'].values[0]) + 'zł     ' + \
                          'Średnia: ' + str(components[components['Component']=='ser']['price_m'].values[0])+ 'zł     ' + \
                          'Mała: ' +str(components[components['Component']=='ser']['price_s'].values[0]) + 'zł     '
        self.ids.ciasto.text = 'Ciasto    Duża: ' + str(
            components[components['Component'] == 'ciasto']['price_l'].values[0]) + 'zł     ' + \
                            'Średnia: ' + str(
            components[components['Component'] == 'ciasto']['price_m'].values[0]) + 'zł     ' + \
                            'Mała: ' + str(
            components[components['Component'] == 'ciasto']['price_s'].values[0]) + 'zł     '

        for x in pizzas_price.index:
            label = Label(text=(str(pizzas_price.iloc[int(x), 0])).capitalize(), size_hint_y=None, height=50,bold=True,color=(0,1,0,1))
            self.ids.calc.add_widget(label)
            label = Label(text=(str(round(pizzas_price.iloc[int(x), 1],2)))+' zł', size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            label = Label(text=(str(round(pizzas_price.iloc[int(x), 2],2)))+' zł', size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            label = Label(text=(str(round(pizzas_price.iloc[int(x), 3],2)))+' zł', size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)

            label = Label(text='', size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)

            tx = str(pizzas.iloc[int(x), 1])
            if tx == 'nan':
                tx = ''
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            tx = str(pizzas.iloc[int(x), 2])
            if tx == 'nan':
                tx = ''
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            tx = str(pizzas.iloc[int(x), 3])
            if tx == 'nan':
                tx = ''
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            tx = str(pizzas.iloc[int(x), 4])
            if tx == 'nan':
                tx = ''
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            tx = str(pizzas.iloc[int(x), 5])
            if tx == 'nan':
                tx = ''
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            tx = str(pizzas.iloc[int(x), 6])
            if tx == 'nan':
                tx = ''
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            tx = str(pizzas.iloc[int(x), 7])
            if tx == 'nan':
                tx = ''
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            tx = str(pizzas.iloc[int(x), 8])
            if tx == 'nan':
                tx = ''
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)
            tx = str(pizzas.iloc[int(x), 9])
            if tx == 'nan':
                tx = ''
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)

            for i in range (0,5):
                label = Label(text='', size_hint_y=None, height=50)

                self.ids.calc.add_widget(label)

            tx = str(components[components['Component'] == 'sos']['price_l'].values[0]) + '/'  + str(
                components[components['Component'] == 'sos']['price_m'].values[0]) + '/'  + str(
                components[components['Component'] == 'sos']['price_s'].values[0]) + '/'  + 'zł'
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)

            com=str(pizzas.iloc[int(x), 2])
            tx = str(components[components['Component'] == com]['price_l'].values[0]) + '/' + str(
                components[components['Component'] == com]['price_m'].values[0]) + '/' + str(
                components[components['Component'] == com]['price_s'].values[0]) + '/' + 'zł'
            label = Label(text=tx, size_hint_y=None, height=50)
            self.ids.calc.add_widget(label)


            com = str(pizzas.iloc[int(x), 3])
            if com =='nan':
                label = Label(text='', size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)
            else:
                tx = str(components[components['Component'] == com]['price_l'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_m'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_s'].values[0]) + '/' + 'zł'
                label = Label(text=tx, size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)

            com = str(pizzas.iloc[int(x), 4])
            if com == 'nan':
                label = Label(text='', size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)
            else:
                tx = str(components[components['Component'] == com]['price_l'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_m'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_s'].values[0]) + '/' + 'zł'
                label = Label(text=tx, size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)

            com = str(pizzas.iloc[int(x), 5])
            if com == 'nan':
                label = Label(text='', size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)
            else:
                tx = str(components[components['Component'] == com]['price_l'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_m'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_s'].values[0]) + '/' + 'zł'
                label = Label(text=tx, size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)

            com = str(pizzas.iloc[int(x), 6])
            if com == 'nan':
                label = Label(text='', size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)
            else:
                tx = str(components[components['Component'] == com]['price_l'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_m'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_s'].values[0]) + '/' + 'zł'
                label = Label(text=tx, size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)

            com = str(pizzas.iloc[int(x), 7])
            if com == 'nan':
                label = Label(text='', size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)
            else:
                tx = str(components[components['Component'] == com]['price_l'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_m'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_s'].values[0]) + '/' + 'zł'
                label = Label(text=tx, size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)

            com = str(pizzas.iloc[int(x), 8])
            if com == 'nan':
                label = Label(text='', size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)
            else:
                tx = str(components[components['Component'] == com]['price_l'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_m'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_s'].values[0]) + '/' + 'zł'
                label = Label(text=tx, size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)

            com = str(pizzas.iloc[int(x), 9])
            if com == 'nan':
                label = Label(text='', size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)
            else:
                tx = str(components[components['Component'] == com]['price_l'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_m'].values[0]) + '/' + str(
                    components[components['Component'] == com]['price_s'].values[0]) + '/' + 'zł'
                label = Label(text=tx, size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)



            for i in range (0,14):
                label = Label(text='', size_hint_y=None, height=50)
                self.ids.calc.add_widget(label)
class WindowManager(ScreenManager):

    pass

Window.maximize()
class CalcApp(App):
    Comp_id = ""

    def build(self):
        pass




if __name__ == "__main__":
    CalcApp().run()