export const fetchMarkdownPosts = async () => {
	const allPostFiles = import.meta.glob("../../md/*.md")
	const iterablePostFiles = Object.entries(allPostFiles)

	const allPosts = await Promise.all(
		iterablePostFiles.map(async ([path, resolver]) => {
			const { metadata } = await resolver()
			const postPath = '/post' + path.slice(8)
			console.log(postPath)

			return {
				meta: metadata,
				path: postPath,
			}
		})
	)

	return allPosts
}