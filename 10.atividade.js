const readline = require('readline-sync')

// estoque.js

let estoque = []; // Lista para armazenar os produtos no estoque

/**
 * Adiciona um novo produto ao estoque.
 * @param {string} nome - O nome do produto.
 * @param {number} preco - O preço do produto.
 * @param {number} quantidade - A quantidade inicial em estoque.
 */
function adicionarProduto(nome, preco, quantidade) {
  const novoProduto = {
    nome: nome,
    preco: preco,
    quantidade: quantidade
  };
  estoque.push(novoProduto);
  console.log(`Produto "${nome}" adicionado ao estoque.`);
}

/**
 * Lista todos os produtos no estoque.
 */
function listarEstoque() {
  if (estoque.length === 0) {
    console.log("O estoque está vazio.");
    return;
  }
  console.log("\n--- Estoque Atual ---");
  estoque.forEach(produto => {
    console.log(`Nome: ${produto.nome}, Preço: R$${produto.preco.toFixed(2)}, Quantidade: ${produto.quantidade}`);
  });
  console.log("----------------------\n");
}

/**
 * Atualiza a quantidade de um produto no estoque.
 * @param {string} nomeProduto - O nome do produto a ser atualizado.
 * @param {number} novaQuantidade - A nova quantidade do produto.
 */
function atualizarEstoque(nomeProduto, novaQuantidade) {
  const produtoEncontrado = estoque.find(produto => produto.nome === nomeProduto);
  if (produtoEncontrado) {
    produtoEncontrado.quantidade = novaQuantidade;
    console.log(`Estoque de "${nomeProduto}" atualizado para ${novaQuantidade}.`);
  } else {
    console.log(`Produto "${nomeProduto}" não encontrado no estoque.`);
  }
}

export { estoque, adicionarProduto, listarEstoque, atualizarEstoque };