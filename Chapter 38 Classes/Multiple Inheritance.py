#Multiple Inheritance
class Animal(object):
    cat = 'cat'

class Bird(object):
    peacock = 'this is the peacock' # we won't see this.
    parot = 'this is the parot'

class AniBird(Animal, Bird):
    var_both = 'Animal and bird'
    
fb = AniBird()
print(fb)



class Foo(object):
    foo = 'attr foo of Foo'
class Bar(object):
    foo = 'attr foo of Bar' # we won't see this.
    bar = 'attr bar of Bar'
class FooBar(Foo, Bar):
    foobar = 'attr foobar of FooBar'
fb = FooBar()
print(fb)
