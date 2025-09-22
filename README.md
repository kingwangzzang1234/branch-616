# branch-616

## TODO

- [git branch buzz]create new branch: buzz

- [git switch buzz]switch branch to buzz
- [vi fizz.py] fizz.py ->
	- 만약 i가 3의 배수는 아닌데, 5의 배수라면 -> "buzz"
```python
for i in range(1,15+1):
    if i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
```
- 저장 후, 테스트(가능하다면)
- [git add fizz.py]
- [git commit]

- [git switch main]switch branch to main
- [git merge buzz]merge branch buzz
- [git branch -D buzz]Delete branch buzz

## --upstream-set
- git push -u origin buzz
- remote에 생성할 새 브랜치 buzz에 대해 트랙킹하도록 설정하는 옵션
- 첫 push 할 때 한번만 쓰면 됨(이후로는 git push origin buzz)
