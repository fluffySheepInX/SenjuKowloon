
% rebase('layout2.tpl', title='千手九龍', year=year, divBaseColor=divBaseColor)

<div class="flexcontainer">
	<div class="flexitem item1">
		<br />
		<br />
		<br />
		Quest001
		<br />
		<form action="./questCommonDetail" method="post">
			<input type="hidden" name="quest_common_cd" value="1" />
			<button class="quest" type="submit">
				<img src="static/quest/quest001.jpg" alt="送信" />
			</button>
		</form>
		<br />
		<br />
		Quest002
		<form action="./questCommonDetail" method="post">
			<input type="hidden" name="quest_common_cd" value="2" />
			<button class="quest" type="submit">
				<img src="static/quest/quest002.jpg" alt="送信" />
			</button>
		</form>
		<br />
		<br />
		Quest003
		<br />
		Quest004
		<br />
		<button type=“button” onclick="location.href='./main'">戻る</button>
	</div>
</div>