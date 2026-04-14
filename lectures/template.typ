// Hide admonition macros instead of importing them
#let admonition(..args) = {}
#let attentionBlock(..args) = {}
#let cautionBlock(..args) = {}
#let dangerBlock(..args) = {}
#let errorBlock(..args) = {}
#let hintBlock(..args) = {}
#let importantBlock(..args) = {}
#let noteBlock(..args) = {}
#let seealsoBlock(..args) = {}
#let tipBlock(..args) = {}
#let warningBlock(..args) = {}

// Hide tablex elements
#let tablex(..args) = {}
#let cellx(..args) = {}
#let tableStyle = {}
#let columnStyle = {}

// Hide all par, enum, and list elements
#show par: none
#show enum: none
#show list: none

// Display headings as paragraph-size text
#show heading: set text(size: 11pt)

// Ignore link content, show only link text
#show link: it => it.body

#set document(
  title: "[-doc.title-]",
  author: "[-doc.authors[0].name-]",
)

#set page(
  paper: "us-letter",
  header: text(weight: "bold", "[-doc.title-]"),
)

#set text(
  font: ("Fira Sans", "Lete Sans Math"),
  lang: "en",
  region: "US",
)

#show math.equation: set text(font: "Fira Math")
#show raw: set text(font: "Fira Mono", size: 1.25em)

[-CONTENT-]
