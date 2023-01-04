
% rebase('layout2.tpl', title='千手九龍', year=year, divBaseColor=divBaseColor)

<div class="flexcontainer">
	<div class="flexitem item1">
		<br />
		防衛を行う部隊を選択してください。
		<br />
		<form action="./commandGuardInput" method="post">
			<br />
			{{!getSoldier}}
			<br />
			<input type="radio" name="soldier" value="LAST">最後に招集した部隊を使用する
			<br />
			<button type="submit">登録</button>
		</form>
		<br />
		<br />
		<button type=“button” onclick="location.href='./main'">戻る</button>
	</div>
</div>