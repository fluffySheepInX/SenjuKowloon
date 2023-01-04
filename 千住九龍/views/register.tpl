
% rebase('layout.tpl', title='千手九龍', year=year)

<div class="flexcontainer">
	<div class="flexitem item1">
		<br />
		<br />
		......貴方は闇の中でまどろむ。
		<br />
		静かで心地いい。......本格的な眠りにつく直前、コール音が鳴り響く。
		<br />
		......貴方は北千住へ向かうことを電話の主に命じられる。
		<br />
		さあ、"千住入り"の準備をしなくては。
		<br />
		<br />
		<form action="./registerUser" method="post" onsubmit="return checkNijyuSubmit();">
			<div class="flexcontainer">
				<div class="flexitem">
					<label>Username</label>
					<br />
					ゲーム中の貴方の名前
				</div>
				<div class="flexitem">
					<input type="text" name="user_name">
				</div>
			</div>
			<br />
			<div class="flexcontainer">
				<div class="flexitem">
					<label>Id</label>
					<br />
					ゲーム中の貴方を識別するId
				</div>
				<div class="flexitem">
					<input type="text" name="user_id">
				</div>
			</div>
			<br />
			<div class="flexcontainer">
				<div class="flexitem">
					<label>Password</label>
					<br />
					明かしてはならない
				</div>
				<div class="flexitem">
					<input type="password" name="user_password">
				</div>
			</div>
			<br />
			<br />
			<div class="flexcontainer">
				<div class="flexitem">
					<label>所属</label>
					<br />
					貴方はどの陣営に所属しているか？
				</div>
				<div class="flexitem">
					<input type="radio" name="user_camp_group" value="1">魔法使い【ソルシエール・アライアンス】
					<br />
					<input type="radio" name="user_camp_group" value="2">半グレ【絶東同盟・関東支部】
					<br />
					<input type="radio" name="user_camp_group" value="3">警察【警視庁警視総監直属・危機管理課】
				</div>
			</div>
			<br />
			<br />
			【所属説明】クリックで展開されます。
			<br />
			<details>
				<summary>
					魔法使い
				</summary>
				<br />
				・特色は戦闘力
				<br />
				・ふざけた力、この世を統べる力
				<br />
				・「この力......使わないと、勿体ない」
			</details>
			<br />
			<details>
				<summary>
					半グレ
				</summary>
				<br />
				・特色は財力
				<br />
				・生まれながらの虎
				<br />
				・「出世こそ我が人生、ってやつだな」
			</details>
			<br />
			<details>
				<summary>
					警察
				</summary>
				<br />
				・特色はバランス
				<br />
				・正義の執行者
				<br />
				・「諸兄らは使命を持ってここに集ったと考える。その使命を果たすように」
			</details>
			<br />
			<br />
			<br />ご登録準備ありがとうございます。
			<br />多重登録(複数キャラの作成)、
			<br />その他社会通念上不適切な行為は控えて頂くようお願い致します。
			<br />
			<br />
			<button id="btnSubmit" type="submit">登録</button>
			<br />
			{{ !message}}
		</form>
		<br />
	</div>
</div>
<script>
function checkNijyuSubmit(){
  var obj = document.getElementById("btnSubmit");
  if(obj.disabled){
    return false;
  }else{
    obj.disabled = true;
    return true;
  }
}
</script>