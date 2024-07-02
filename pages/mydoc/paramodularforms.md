---
title: Paramodular forms
tags: #[getting_started, formatting, content_types]
keywords: #posts, blog, news, authoring, exclusion, frontmatter
last_updated: #Feb 25, 2016
summary: #"You can use posts when you want to create blogs or news type of content."
sidebar: mydoc_sidebar
permalink: paramodular.html
folder: mydoc
---

## Notes
To do 

## Cheat Sheet

[Cheat sheet on paramodular forms (Cris Poor)](files/paramodular_cs.pdf)

## 

## Code

#### Pari-GP

```yaml
---
to do
---
```

#### SageMath

```yaml
---
to do
---
```




<!--| Frontmatter | Required? | Description |
|-------------|-------------|-------------|
| **title** | Required | The title for the page |
| **tags** | Optional | Tags for the page. Make all tags single words, with underscores if needed. Separate them with commas. Enclose the whole list within brackets. Also, note that tags must be added to \_data/tags_doc.yml to be allowed entrance into the page. This prevents tags from becoming somewhat random and unstructured. You must create a tag page for each one of your tags following the sample pattern in the tabs folder. (Tag pages aren't automatically created.)  |
| **keywords** | Optional | Synonyms and other keywords for the page. This information gets stuffed into the page's metadata to increase SEO. The user won't see the keywords, but if you search for one of the keywords, it will be picked up by the search engine.  |
| **sidebar** | Required | Refers to the sidebar data file for this page. Don't include the ".yml" file extension for the sidebar &mdash; just provide the file name. If no sidebar is specified, this value will inherit the `default` property set in your \_config.yml file for the page's frontmatter. |
| **permalink**| Required | This theme uses permalinks to facilitate the linking. You specify the permalink want for the page, and the \_site output will put the page into the root directory when you publish. Follow the same convention here as you do with page permalinks -- list the file name followed by the .html extension. |
| **summary** | Optional | A 1-2 word sentence summarizing the content on the page. This gets formatted into the summary section in the page layout. Adding summaries is a key way to make your content more scannable by users (check out [Jakob Nielsen's site](http://www.nngroup.com/articles/corporate-blogs-front-page-structure/) for a great example of page summaries.) The only drawback with summaries is that you can't use variables in them. |

-->

