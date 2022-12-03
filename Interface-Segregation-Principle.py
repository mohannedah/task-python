class IOrderService:

    def orderBurger(quantity):
        pass


    def orderFries(quantity):
        pass;    



class OrderBurger(IOrderService):

    def orderBurger(quantity):
        print("Recieved burger of quantity " + quantity)

    def orderFries(quantity):
        raise NotImplementedError



# OrderBurger implements IOrderService which has all the methods concerned with the orders and needs to be implemented in all of the sub-classes
# OrderBurger only worries about the orderBurger method and doesn't need to implement the orderFries method.


class IOrderBurger:
    def orderBurger(quantity):
        pass



class IOrderFries:

    def orderFries(quantity):
        pass


class OrderBurger(IOrderBurger):

    def orderBurger(quantity):
        print("Recieved burger of quantity " + quantity)


class OrderFries(IOrderFries):
    def orderFries(quantity):
        print("Recieved Fries of quantity " + quantity)





