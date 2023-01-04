
% rebase('layout2.tpl', title='千手九龍', year=year, divBaseColor=divBaseColor)

<div class="flexcontainer">
	<div class="flexitem item1">
		<br />
		<form action="./commandMoveInput" method="post">
			<br />
			{{!getSelectBoxMove}}
			<br />
			{{!getMap}}
			<br />
			<button type="submit">登録</button>
		</form>
		<br />
		<br />
		<button type=“button” onclick="location.href='./main'">戻る</button>
	</div>
</div>