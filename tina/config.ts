import { defineConfig } from "tinacms";

// Your hosting provider likely exposes this as an environment variable
const branch = process.env.HEAD || process.env.VERCEL_GIT_COMMIT_REF || "main";

export default defineConfig({
  branch,
  clientId: "gamer", // Get this from tina.io
  token: null, // Get this from tina.io

  build: {
    outputFolder: "admin",
    publicFolder: "static",
  },
  media: {
    tina: {
      mediaRoot: "",
      publicFolder: "static",
    },
  },
  schema: {
    collections: [
      {
        name: "post",
        label: "Posts",
        path: "content",
        format: 'md',
        fields: [
          {
            type: "datetime",
            name: "date",
            label: "date",
            required: true,
          },
          {
            type: "string",
            name: "tags",
            label: "Tag",
            isTitle: false,
            required: true,
          },
          {
            type: "string",
            name: "title",
            label: "Title",
            isTitle: true,
            required: true,
          },
          {
            type: "rich-text",
            name: "excerpt",
            label: "Excerpt",
            isBody: false,
          },
          {
            type: "rich-text",
            name: "body",
            label: "Body",
            isBody: true,
          },
          {
            type: "image",
            name: "image",
            label: "image",
            isBody: false,
          },
          {
            type: "string",
            name: "authors",
            label: "Author",
            isTitle: false,
            required: true,
          },
        ],
      },
    ],
  },
});
