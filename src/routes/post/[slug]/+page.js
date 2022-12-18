// src/routes/post/[slug]/+page.js
export async function load({ params }){
  const post = await import(`../../../md/${params.slug}.md`)
  const { title, date, author, words } = post.metadata
  const content = post.default
  return {
    content,
    title,
    date,
		author,
		words,
  }
}