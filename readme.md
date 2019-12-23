<table>
	<thead>
		<tr>
			<th colspan="5" style="text-align: center;"><strong>Subjects of Study</strong></th>
		</tr>
		<tr>
			<td colspan="5">The links below are to the parent GitHub repos of completed courses, resources, my own notes, links to articles, etc. about the topics shown below. They are designed to be my "go-to" place for teaching myself the given subject.</td>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><a href="https://github.com/coolinmc6/analytics">Analytics</a></td>
			<td><strong><em><a href="https://github.com/coolinmc6/CS-concepts">Computer Science</a></em></strong></td>
			<td><a href="https://github.com/coolinmc6/design-ux-ui#product-design--development">Product Development</a></td>
			<td><a href="https://github.com/coolinmc6/design-ux-ui">UX / UI Design</a></td>
			<td><a href="https://github.com/coolinmc6/front-end-dev">Front End Development</a></td>
		</tr>
		<tr>
			<td></td>
			<td><em>Design of Computer Problems</em></td>
			<td></td>
			<td></td>
			<td></td>
		</tr>		
	</tbody>
</table>

<a name="top"></a>

# Design of Computer Problems

Coursework for [Udacity's Design of Computer Programs](https://www.udacity.com/course/design-of-computer-programs--cs212).

## Lesson 1

```py
print(max([3,4,-5,0], key=abs))
```
- with `max()`, we can choose which function evaluates the values. In this example, we are using
the absolute value function, `abs()`, to evaluate those numbers: so -5 has one of the highest 
absolute values.
- We apply this concept to our poker program:

```py
def poker(hands):
  "Return the best hand"
  return max(hands, key=hand_rank)
```
- we now need to write a function, `hand_rank`, which ranks the hands appropriately

### Sources and Code Checks

- [https://github.com/wentaocn/Design-of-Computer-Programs/](https://github.com/wentaocn/Design-of-Computer-Programs/)
- [https://github.com/jrleszcz/design-of-computer-programs](https://github.com/jrleszcz/design-of-computer-programs)
- [https://github.com/aceofall/Design-of-Computer-Programs-1](https://github.com/aceofall/Design-of-Computer-Programs-1)
