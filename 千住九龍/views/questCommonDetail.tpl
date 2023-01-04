
% rebase('layout2.tpl', title='千手九龍', year=year, divBaseColor=divBaseColor)

<div class="flexcontainer">
	<div class="flexitem item1">
		<br />
		<br />
		{{! quest }}
		<br />
		<br />
		～Quest～
		<br />
		{{! conditions }}
		<br />
		{{! executeQuestButton }}
		<br />
		{{! resultCheck }}
		<br />
		<br />
		<br />
		{{! resultQuest }}
		<br />
		<form action="./questCommon" method="post">
			<button type="submit">戻る</button>
		</form>
		<br />
	</div>
</div>