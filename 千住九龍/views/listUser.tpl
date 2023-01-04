
% rebase('layout.tpl', title='千手九龍', year=year)

<div class="flexcontainer">
	<div class="flexitem item1">
		<br />
		登録者情報
		<br />
		<br />
		*以下にある項目はクリックで展開されます
		<br />
		<br />
		<details>
			<summary>
				魔法使い
			</summary>
			<br />
			{{ !magic }}
			<br />
		</details>
		<br />
		<details>
			<summary>
				半グレ
			</summary>
			<br />
			{{ !outlaw }}
			<br />
		</details>
		<br />
		<details>
			<summary>
				警察
			</summary>
			<br />
			{{ !police }}
			<br />
		</details>
		<br />
		<br />
		<button type=“button” onclick="location.href='./top'">戻る</button>
	</div>
</div>