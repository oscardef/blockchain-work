// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract OscarToken is ERC20 {
    mapping(address => uint256) public balances;
    mapping(address => mapping(address => uint256)) public allowed;

    uint256 private _totalSupply;

    constructor() ERC20("OscarToken", "OT") {
        _mint(msg.sender, 1000000 * (10**decimals()));
        _totalSupply += 1000000 * (10**decimals());
    }

    function balanceOf(address user) public view override returns (uint256) {
        return balances[user];
    }

    function decimals() public view virtual override returns (uint8) {
        return 18;
    }

    function _mint(address account, uint256 amount) internal override {
        require(account != address(0), "Cannot mint to the zero address");
        _totalSupply += amount;
        balances[msg.sender] += amount;

        emit Transfer(address(0), account, amount);
    }

    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        require(from != address(0), "Transfer from the zero address");
        require(to != address(0), "Transfer to the zero address");
        require(amount != 0, "Can't transfer 0 tokens");
        require(
            amount <= balances[msg.sender],
            "You don't have this many tokens to transfer"
        );
        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
    }

    function transfer(address to, uint256 amount)
        public
        override
        returns (bool)
    {
        _transfer(msg.sender, to, amount);

        return true;
    }

    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override returns (bool) {
        uint256 currAllowance = allowance(from, msg.sender);
        require(currAllowance >= amount, "Insufficient allowance");
        _approve(from, to, currAllowance - amount);
        _transfer(from, to, amount);
        return true;
    }

    function approve(address spender, uint256 amount)
        public
        override
        returns (bool)
    {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal override {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");
        allowed[owner][spender] = amount;

        emit Approval(owner, spender, amount);
    }

    function allowance(address owner, address spender)
        public
        view
        override
        returns (uint256)
    {
        return allowed[owner][spender];
    }
}
