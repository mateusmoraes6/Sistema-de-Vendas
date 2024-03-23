# Desenvolvimento de Sistema de Vendas: Esboço inicial

Como desenvolvedor em uma consultoria de software, você está encarregado de iniciar a implementação de um sistema de vendas. O sistema atenderá a três tipos de clientes: pessoas físicas (PF) frequentes, pessoas físicas esporádicas e pessoas jurídicas (PJ).

**Funcionalidades Principais:**

1. **Restrições de Compra:** Clientes PF não VIPs podem comprar até 20 itens, enquanto clientes PJ podem adquirir até 50 itens. Clientes VIPs têm acesso ilimitado.
2. **Cupom de Desconto:** Cada tipo de cliente terá um cupom de desconto associado. VIPs: 20% de desconto, PF esporádicos: 5% de desconto, e PJ: 10% de desconto.
3. **Encapsulamento de Desconto:** Os cupons de desconto serão encapsulados em métodos para facilitar a aplicação nas compras.

**Diagrama de Classes:** Os engenheiros de software forneceram um diagrama de classes que representa a estrutura do sistema, incluindo as classes `Cliente`, `ClientePF`, `ClientePJ`, `ClienteVIP` e métodos associados.

**Desafio:** Sua missão é implementar o esboço inicial do sistema com base no diagrama de classes fornecido. A solução deve garantir a aplicação correta das restrições de compra e dos descontos associados a cada tipo de cliente.

**Resolução: Implementação das Classes**

Para resolver este desafio, serão implementadas quatro classes: uma classe base e três subclasses, cada uma representando um tipo de cliente. Os atributos comuns a todas as classes serão definidos na classe base, enquanto os atributos específicos serão implementados nas subclasses.

**Implementação das Classes:**

1. **Classe Base (`Cliente`):** Esta classe conterá os atributos e métodos comuns a todos os tipos de clientes.
2. **Subclasses (`ClientePF`, `ClientePJ`, `ClienteVIP`):** Cada subclasse representará um tipo específico de cliente e terá seus próprios atributos e métodos específicos.

**Método `realizar_compra`:** O método `realizar_compra` será sobrescrito em cada subclasse para acomodar a restrição de compra específica de cada tipo de cliente.

**Cupom de Desconto:** O cupom de desconto também será implementado em cada subclasse de acordo com as especificidades de desconto para cada tipo de cliente.

**Possível Implementação:** A seguir, é apresentada uma implementação sugerida para a solução, demonstrando a estrutura das classes e como os métodos podem ser sobrescritos e aplicados para atender aos requisitos do desafio.
