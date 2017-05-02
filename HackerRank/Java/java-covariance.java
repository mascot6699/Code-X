class Flower{
    String whatsYourName() {
        return getClass().getSimpleName();
    }
}

class Jasmine extends Flower{

}
class Lily extends Flower{

}
class Lotus extends Flower{

}

class State{
    Flower yourNationalFlower(){
        return new Flower();
    }
}

class WestBengal extends State{
    @Override
    Jasmine yourNationalFlower(){
        return new Jasmine();
    }
}
class Karnataka extends State{
    @Override
    Lotus yourNationalFlower(){
        return new Lotus();
    }
}
class AndhraPradesh extends State{
    @Override
    Lily yourNationalFlower(){
        return new Lily();
    }
}
