CoffeeScript
++++++++

CoffeeScript is a language which compiles into JavaScript, and it (theoretically) complements the JavaScript usage of Agility.js (MVClets) and jQuery. It runs as a node.js utility (how many Internet frameworks do I need?) and PyOfWave will provide a shell script which will wrap CoffeeScript in two modes:

1) *Development* is pretty-printed and recompiles when you save your CoffeeScript. 
2) *Production* is one off and whitespace is `tr`'ed. 

Out of lack of a very quick overview reference, the rest of this file will be one. 

Syntax
======

Italics are arbitrary bits of the syntax. Syntax surrounded by [ & ] are optional. Exp is short for expression. 

Basic
------

CoffeeScript makes use of whitespace for block delimitation (in POW 2 spaces), this is as opposed to `{` and `}` in JavaScript. New lines delimitate expressions instead of `;`, but if you want to continue an expression, continue it in a new block. 

<table>
<tr><th>Syntax</th>            <th>Action</th></tr>
<tr><td>*var*</td>                 <td>Looks up variable *var* and define in scope if needed (no `var`)</td></tr>
<tr><td>`.`*prop*</td>           <td>Looks up property *prop* on previous object. </td></tr>
<tr><td>`[`*exp*`]`</td>        <td>Looks up result of running expression. </td></tr>
<tr><td>`(`*exps*`)`</td>      <td>Executes previous object as a function, passing it comma separated *exps*</td></tr>
<tr><td>` `*exps*</td>          <td>" "                                              " "</td></tr>

<tr><td>`@`</td>                   <td>Shortcut for `this[`.`]. </td></tr>
<tr><td>`::`</td>                     <td>Shortcut for `.prototype.`. </td></tr>
<tr><td>`?`</td>                    <td>Existential operator. Various usage centering around "is the property defined?"</td></tr>
<tr><td>`(`*exp*`)`</td>        <td>Executes *exp* before anything else. </td></tr>
<tr><td>`#` *. . .*</td>           <td>Comment. (also between `###`s). </td></tr>
</table>

Data Types
-----------

<table>
<tr><th>Syntax</th>                     <th>Class</th>           <th>Description</th></tr>
<tr><td>[`(`*exps*`)`] `->`</td>    <td>Function</td>    <td>Callable code from inline or indented code, accepting array-like arguments *exps*. </td></tr>
<tr><td>[`(`*exps*`)`] `=>`</td>              <td></td>           <td>The "fat arrow" keeps the external block's definition of `this`</td></tr>

<tr><td>`[`*exps*`]`</td>                <td>Array</td>         <td>Stores the value of *exps*, separated by newlines and commas. </td></tr>
<tr><td>-     *exp*...</td>                        <td></td>                <td>Indicates a "splat", a "greedy" object which takes all the rest of the items when on other side of a literal array assignment. </td></tr>
<tr><td>-     *num1*`..[.]`*num2*</td>         <td></td>         <td>Makes the array a "range", containing all values between num1 & num2. 
                                                          <br />Extra dot indicates exclusion of num2. May be used in accesses to get a subset. </td></tr>
<tr><td>[`{`]*key*`:`*val*`,`*. . .*[`}`]</td>   <td>Object</td>        <td>Arbitrary object with specified properties of *key* s = *val* s
                                  <br />Newlines may be used in stead of `,`, providing indentation. </td></tr>

<tr><td>`"`*text*`"`</td>                 <td>String</td>         <td>Stores a sequence of characters. Whitespace collapsed. 
             <br />Also uses `'` and `"""` or `'''` (includes whitespace). </td></tr>
<tr><td>-      `#{`*exp*`}`</td>                 <td></td>             <td>Contained within strings to insert value of *exp*.</td></tr> 
<tr><td>*number*</td>                    <td>Number</td>      <td>Stores a mathematical number. </td></tr>
<tr><td>(as in JS)</td>                  <td>Regex</td>        <td>String analyzation tool. `///` ignores whitespace. </td></tr>
</table

Operators
----------

Operators, like in JS, perform an action on one or two expressions, *exp1* & *exp2*. 

Operator           Description
=                          Sets first expression to the value of the second. 
    When *exp1* is a literal object or array, assigns all variables in *exp1* to values of *exp2*. 
*op*=                  Shortcut for *exp1* `=` *exp1* *op* *exp2*
+ - * / %          Math operators (+ also concats on strings). 

< > == != >=     Comparison operators. (can be chained as in Python). 
>= is isn't of
and or && ||    Boolean logic operators. 
not ! 
in                         Is the value *exp1* in *exp2*?
of                        Is the property *exp1* in *exp2*?

do                        Executes following function with parameters as arguments. 

Branching
----------

Follows the syntax either:

*action* [*conditional*] block|`then` *code*

OR

*code* *action* [*conditional*]

*Action*          Description
if                       Executes *code* only if required *conditional* is true. 
else                  Executes *code* if previous if was false. 
for                    With conditional in format *var* `in` *array*, assigns each value in *array* (or object) to *var* then executes *code*
                          Returns an array of last value in *code*. 
    `of` replaces `in` and loops over keys not values, second *var* after comma is the value. 
    `by` controls the increase of *var* when looping over a range. 
while                  Repeats *code* until *conditional* is false. Returns an Array of the values for each iteration. 
until                   Repeats *code* until *conditional* is true. Returns same as while. 

try                     Forwards any `throw`n "errors" in *code* to following `catch`. 
catch                Preceded by `try` runs if an error (assigned to *conditional*) is `throw`n. 
finally               Executes after try/catch. 

switch             Contains `when`s and `else`. 
when                Executes *code* if `switch`'s *expression* is this *expression*. 
else                  Executes if any `when`s are false