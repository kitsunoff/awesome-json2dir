-- Rewrite repository-relative links for the website.
-- Links to documents that become pages point to those pages; other
-- relative links point to the file on GitHub.

local blob = "https://github.com/kitsunoff/awesome-json2dir/blob/main/"
local raw = "https://raw.githubusercontent.com/kitsunoff/awesome-json2dir/main/"

local pages = {
  ["README.md"] = "index.html",
  ["spec/rfc-json2dir.md"] = "rfc.html",
  ["MANIFESTO.md"] = "manifesto.html",
  ["conformance/README.md"] = "conformance.html",
  ["CONTRIBUTING.md"] = "contributing.html",
}

local source = ""

local function resolve(base, relative)
  local parts = {}
  for part in (base .. relative):gmatch("[^/]+") do
    if part == ".." then
      table.remove(parts)
    elseif part ~= "." then
      table.insert(parts, part)
    end
  end
  return table.concat(parts, "/")
end

local function rewrite(target, prefix)
  if target:match("^%a[%w+.-]*:") or target:match("^#") or target == "" then
    return target
  end
  local path, fragment = target:match("^([^#]*)(.*)$")
  local base = source:match("^(.*/)") or ""
  local resolved = resolve(base, path)
  if pages[resolved] then
    return pages[resolved] .. fragment
  end
  return prefix .. resolved .. fragment
end

return {
  {
    Meta = function(meta)
      source = pandoc.utils.stringify(meta.source or "")
    end,
  },
  {
    Link = function(element)
      element.target = rewrite(element.target, blob)
      return element
    end,
    Image = function(element)
      element.src = rewrite(element.src, raw)
      return element
    end,
  },
}
