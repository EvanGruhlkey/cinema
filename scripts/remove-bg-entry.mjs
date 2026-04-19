import { removeBackground } from "@imgly/background-removal";

export async function stripHeadBackground(file) {
  return removeBackground(file, {
    model: "isnet_quint8",
    output: { format: "image/png", type: "foreground" },
  });
}
