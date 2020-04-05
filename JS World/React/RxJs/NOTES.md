Notes
--------


- `subscription.unsubscribe();` to cancel a subscription
- You can add another observer as a child subscription by `ob1.add(ob2)` Now if you cancel one other too will get cancelled.
- Hot/Cold/Warm Observables
- A Subject, in contrast to an observable, is simply an observer that's also able to emit values. It's both an observable and an observer simultaneously
- events are received after it is created.
- BehaviourSubject => BehaviorSubject is a special type of Subject whose only different is that it will emit the last value upon a new observer's subscription.
- ReplaySubject => ReplaySubject allows you to dispatch any designated number of values.(first argument)
- ReplaySubject accepts an optional second argument upon creation, which is referred to as the window time, and it's defined in milliseconds. 
- AsyncSubject => AsyncSubject only emits the very last value, and will only do so once .complete() has been called on the subject.


-------------

- Operators
    - methods that you can use on Observables (and Subjects) that allow you to change the original observable in some manner and return a new observable.
    - doesn't change old one, just returns new one
    - 2 types
        - static => 
        - instance => 
    - [lots of operator](http://reactivex.io/rxjs/manual/overview.html#categories-of-operators)
    - [Example of merge](https://coursetro.com/posts/code/150/RxJS-Operators-Tutorial---Learn-How-to-Transform-Observables)

---------

