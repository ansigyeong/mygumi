<template>
	<form class="articleform">
		<header class="review-header">
			<i class="icon ion-md-close" @click="goToLocation"></i>
			<p class="header-title">후기 작성</p>
			<p class="header-back" @click="submit">작성</p>
		</header>
		<section class="articleform-title">
			<p class="location-title">📃 {{ location }}</p>
			<input
				id="title"
				class="articleform-title__input"
				type="text"
				v-model="title"
				placeholder="제목을 입력해주세요 😃"
			/>
			<p class="title-limit">{{ lenTitle }}/20</p>
		</section>
		<section class="articleform-wrap">
			<div class="editor">
				<editor-menu-bar :editor="editor" v-slot="{ commands }">
					<div class="menubar">
						<button
							type="button"
							class="menubar__button"
							@click="showImagePrompt(commands.image)"
						>
							<img class="icon" src="@/assets/images/icons/image.svg" />
						</button>
					</div>
				</editor-menu-bar>
				<editor-content class="editor__content" :editor="editor" />
			</div>
		</section>
	</form>
</template>

<script>
import { Editor, EditorContent, EditorMenuBar } from 'tiptap';
import { Image, Placeholder } from 'tiptap-extensions';
import { submitArticle } from '@/api/review';
import { location } from '@/api/tour';

export default {
	components: {
		EditorContent,
		EditorMenuBar,
	},
	props: {
		status: String,
		locationId: String,
	},
	data() {
		return {
			editor: null,
			title: '',
			location: null,
		};
	},
	mounted() {
		this.fetchData();
	},
	methods: {
		async fetchTitle() {
			const { data } = await location(this.locationId);
			this.location = data.data.place;
		},

		showImagePrompt(command) {
			const src = prompt('Enter the url of your image here');
			if (src !== null) {
				command({ src });
			}
		},
		goToLocation() {
			this.$router.push(`/location/${this.locationId}`);
		},
		fetchData() {
			this.fetchTitle();
			const tempEditor = new Editor({
				extensions: [
					new Image(),
					new Placeholder({
						emptyEditorClass: 'is-editor-empty',
						emptyNodeClass: 'is-empty',
						emptyNodeText: '소중한 후기 부탁드릴께요 :)',
						showOnlyWhenEditable: true,
						showOnlyCurrent: true,
					}),
				],
			});
			this.editor = tempEditor;
		},
		async submit() {
			try {
				if (this.status === 'create') {
					const res = await submitArticle({
						title: this.title,
						content: this.editor.getHTML(),
						place: parseInt(this.locationId),
					});
					if (res.status === 201) {
						alert('작성완료');
						this.$router.push(
							`/location/${this.location}/reviews/${res.data.id}/`,
						);
					}
				}
				// if (this.status == 'update') {
				// 	const res = await updateArticle({
				// 		title: this.title,
				// 		content: this.editor.getHTML(),
				// 	});
				// 	if (res.status === 201) {
				// 		alert('작성완료');
				// 		this.$router.push({
				// 			name: 'ArticleDetail',
				// 			params: {
				// 				ariticleId: res.data.id,
				// 			},
				// 		});
				// 	}
				// }
			} catch (error) {
				if (error.response) {
					if (error.response.status === 400) {
						alert('잘못된 요청입니다.');
					} else if (error.response.status === 500) {
						alert('서버가 요청을 처리할 수 없습니다.');
					} else if (error.response.status === 401) {
						alert('로그인 정보를 확인해주세요.');
					} else {
						alert(
							`오류입니다. (status: ${error.response.status}) 문의해주세요.`,
						);
					}
				} else {
					alert(error);
				}
			}
		},
	},
	beforeDestroy() {
		this.editor.destroy();
	},
	computed: {
		lenTitle() {
			let lenTitle = this.title.length;
			return lenTitle;
		},
	},
};
</script>

<style lang="scss">
.editor p.is-editor-empty:first-child::before {
	content: attr(data-empty-text);
	float: left;
	color: #aaa;
	pointer-events: none;
	height: 0;
}
.icon {
	position: relative;
	display: inline-block;
	vertical-align: middle;
	width: 0.8rem;
	height: 0.8rem;
	margin: 0 0.3rem;
	top: -0.05rem;
	fill: currentColor;

	&__svg {
		display: inline-block;
		vertical-align: top;
		width: 100%;
		height: 100%;
	}

	&:first-child {
		margin-left: 0;
	}

	&:last-child {
		margin-right: 0;
	}
}

// svg sprite
body > svg,
.icon use > svg,
symbol {
	path,
	rect,
	circle,
	g {
		fill: currentColor;
		stroke: none;
	}

	*[d='M0 0h24v24H0z'] {
		display: none;
	}
}

.review-header {
	display: flex;
	justify-content: space-between;
	align-items: center;
	border-bottom: 1px solid $lightGray;
	position: sticky;
	top: 0;
	height: 3rem;
	.ion-md-close {
		font-size: 1.5rem;
		transform: translate(50%, -50%);
		margin-left: 10px;
	}
	.header-title {
		font-weight: bold;
	}
	.header-back {
		margin-right: 10px;
	}
}
.articleform-title {
	width: 94%;
	margin-left: 3%;
	margin-right: 3%;
	margin-bottom: 20px;
	margin-top: 20px;
	position: relative;
	.location-title {
		margin-bottom: 1rem;
		margin-left: 1rem;
	}
	.articleform-title__input {
		width: 100%;
		border-bottom: 1px solid $lightGray;
		height: 40px;
		font-size: 1.5rem;
		padding: 10px;
		margin-bottom: 5px;
		white-space: nowrap;
	}
	.title-limit {
		color: lightGray;
		position: absolute;
		right: 0;
	}
}

.articleform-wrap {
	margin-left: 3%;
	margin-right: 3%;
	width: 100%;
	display: flex;
	flex-direction: column;
	padding: 1rem;
}
.editor {
	@import '~@/assets/styles/main.scss';
	margin: 0;
	width: 100%;
	max-width: 100%;
	display: flex;
	flex-direction: column;
	.editor__content {
		width: 100%;
		height: 400px;
		overflow-y: scroll;
	}
}

.head-label {
	display: block;
}
.articleform-head {
	display: flex;
	justify-content: flex-end;
	align-items: center;
	margin-bottom: 0.5rem;
	h2 {
		margin-bottom: 0;
	}
}
</style>
