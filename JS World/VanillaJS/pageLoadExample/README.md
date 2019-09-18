Here we learn how we can make the DOM load time really fast even if our 
JS is big by using a trick.. ssshhhhh

- It has these two imp code snippet in HEAD tag
- We use `P.register` to signal some library is loaded
- We use `P.when` and wait for the above signals and if satisfied 


Things to observe from above example
- As code3 is slow whole DOM is not waiting for it
- `logging.js` just waits for `code1.js` and `code2.js` to load
- `homepage.js` waits for `code1.js`, `code2.js`, `code2.js` and so 
although written above is called at last as had to wait for long code in `code3.js`.

