
% rebase('layout2.tpl', title='千手九龍', year=year, divBaseColor=divBaseColor)

<div class="flexcontainer">
	<div class="flexitem item1">
		{{!message}}
		<br />
		<br />****
		<br />招集で必要な金額は
		<br />((招集人数 - 統率力) * Cost) + ((統率力* Cost)/{{!cost}} )
		<br />となります。
		<br />つまり、統率力の分だけコストが安くなり、
		<br />統率力を越える分は通常のコストとなります。
		<br />****
		<br />
		<br />
		{{!getSoldier}}
		<br />
		<br />
		<button type=“button” onclick="location.href='./main'">戻る</button>
	</div>
</div>