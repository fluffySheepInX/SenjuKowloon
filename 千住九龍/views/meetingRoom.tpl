
% rebase('layout2.tpl', title='千手九龍', year=year, divBaseColor=divBaseColor)

<div class="flexcontainer">
	<div class="flexitem item1">
		<button type=“button” onclick="location.href='./main'">戻る</button>
		<br />
		<br />戦場から事務所に戻った貴方は部下たちに迎えられる。
		<br />お疲れ様です、ご苦労様です......
		<br />さて、何から確認致しましょうか？
		<br />
		<br />****
		<br />この画面はチャット等で決まった重要事項"等"をまとめるのに良い場所です。
		<br />"等"？はい、プレイヤーご自身で使い方をお決めになられるとよろしいかと思います。
		<br />****
		<br />
		<form action="./inputMeetingRoom" method="post">
			<br />
			題
			<br />
			<input type="text" name="title" size="40" maxlength="20">
			<br />
			本文
			<br />
			<textarea cols="30" rows="10" name="body"></textarea>
			<br />
			<button type="submit">送信</button>
		</form>
		<br />
		{{ !body }}
		<br />
		<button type=“button” onclick="location.href='./main'">戻る</button>
	</div>
</div>