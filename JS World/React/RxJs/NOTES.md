Notes
--------


- `subscription.unsubscribe();` to cancel a subscription
- You can add another observer as a child subscription by `ob1.add(ob2)` Now if you cancel one other too will get cancelled.
- Hot/Cold/Warm Observables
- A Subject, in contrast to an observable, is simply an observer that's also able to emit values. It's both an observable and an observer simultaneously
- events are received after it is created.
- BehaviourSubject => BehaviorSubject is a special type of Subject whose only different is that it will emit the last value upon a new observer's subscription.
- ReplaySubject => ReplaySubject allows you to dispatch any designated number of values.
